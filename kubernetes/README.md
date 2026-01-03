kubectl exec -it <pod name> -- bash
apt-get update && apt-get install -y iputils-ping
ping -c 3 <pod ip> # to check if the traffic is accepting

hostname -I




You: kubectl create deployment nginx

Step 1: kubectl → apiserver (HTTP POST request)

Step 2: apiserver 
   - Authenticates (are you who you say you are?)
   - Authorizes (are you allowed to create deployments?)
   - Validates (is this YAML correct?)
   - Stores in etcd: {"deployment": "nginx", "replicas": 3}

Step 3: Deployment Controller (watching apiserver)
   - Sees new deployment in etcd
   - Creates ReplicaSet
   - Stores ReplicaSet in etcd (via apiserver)

Step 4: ReplicaSet Controller (watching apiserver)
   - Sees new ReplicaSet in etcd
   - Creates 3 Pod objects
   - Stores Pods in etcd (via apiserver)
   - Pods are in "Pending" state (no node assigned yet)

Step 5: Scheduler (watching apiserver)
   - Sees Pods in "Pending" state
   - Scores all nodes (CPU, memory, affinity rules)
   - Picks best node for each Pod
   - Updates Pod in etcd: {"pod": "nginx-abc", "node": "worker-1"}

Step 6: Kubelet on worker-1 (polling apiserver every 10s)
   - Asks apiserver: "Any Pods for me?"
   - Apiserver responds: "Yes, run nginx-abc"
   - Kubelet calls CNI plugin: "Create network for this Pod"
   - CNI assigns IP: 10.244.1.5
   - Kubelet calls container runtime: "Start nginx container"
   - Container runtime pulls image, starts container

Step 7: Kubelet reports back
   - Updates Pod status in etcd (via apiserver)
   - {"pod": "nginx-abc", "status": "Running", "ip": "10.244.1.5"}

Step 8: ReplicaSet Controller
   - Sees Pod is Running
   - Checks: Desired (3) == Actual (3) ✅
   - Stops reconciling (nothing to do)