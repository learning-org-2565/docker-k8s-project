# How to Check Where Your Volume Data Is Stored

## 1. Find which Node the Pod is running on
```bash
kubectl get pods -o wide
```
Look at the `NODE` column.

## 2. Get detailed Pod info (see volume paths)
```bash
kubectl describe pod <your-postgres-pod-name>
```
Look for the "Volumes:" section.

## 3. SSH into the Node (if you have access)
```bash
# For Minikube
minikube ssh

# For cloud providers (GKE, EKS, AKS)
# You usually can't SSH directly for security reasons
```

## 4. Find the actual storage location on the Node
```bash
# Once inside the Node
sudo ls /var/lib/kubelet/pods/

# Find your pod's UID from kubectl describe output
# Then navigate to:
# /var/lib/kubelet/pods/<POD_UID>/volumes/kubernetes.io~empty-dir/postgres-storage/
```

## 5. Easier way: Execute command inside the container
```bash
# Check the mounted path from inside the container
kubectl exec -it postgres-db-689d49767d-xglxl -- ls -la /var/lib/postgresql/data

# See what's stored
kubectl exec -it <postgres-pod-name> -- df -h /var/lib/postgresql/data



```

## Example Output
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G  2.1G   48G   5% /var/lib/postgresql/data
```
This shows it's using the Node's disk.
