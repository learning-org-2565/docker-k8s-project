1. ✅ ReplicaSet maintains desired state
2. ✅ Uses label selectors to find Pods
3. ✅ Doesn't care WHO created Pods
4. ✅ Adopts existing Pods with matching labels
5. ✅ Deletes YOUNGEST Pods first when scaling down
6. ✅ Control loop runs continuously


✅ REPLICASET - COMPLETE UNDERSTANDING
You now know:
1. ✅ ReplicaSet maintains DESIRED NUMBER only
2. ✅ Does NOT update existing Pods
3. ✅ New template only affects NEW Pods
4. ✅ Manual deletion needed to update all Pods
5. ✅ This limitation → Why Deployments existl