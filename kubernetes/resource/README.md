# Real-time pod usage
kubectl top pods -n production

# See which pods consuming most
kubectl top pods -A --sort-by=memory
kubectl top pods -A --sort-by=cpu

# Node pressure check
kubectl describe nodes | grep -A 5 "Conditions:"
# Look for: MemoryPressure, DiskPressure

# Pod resource consumption over time (if metrics-server + prometheus)
# Check Grafana dashboards for:
# - CPU throttling events
# - Memory usage trends
# - OOMKill count
```

---

### **2. When to Adjust Resources (Decision Framework)**
```
INCREASE REQUESTS when:
├─ Pods frequently pending (insufficient resources)
├─ Multiple pods on same node competing
└─ Scheduler placing pods poorly

INCREASE LIMITS when:
├─ Frequent OOMKilled events
├─ CPU throttling during normal operation
└─ Performance degradation under load

DECREASE REQUESTS when:
├─ Actual usage consistently < 50% of requests
├─ Wasting node capacity
└─ Could fit more pods per node

DECREASE LIMITS when:
├─ Never reaching limits (usage < 60% of limits)
├─ Want to prevent resource hogging
└─ Enforce strict boundaries
```

---

### **3. Common Mistakes (Avoid These!)**
```
❌ MISTAKE 1: Setting requests = limits for all workloads
   ✅ FIX: Only use Guaranteed for critical services

❌ MISTAKE 2: Guessing resources without measurement
   ✅ FIX: Always deploy without limits first, measure, then configure

❌ MISTAKE 3: Setting requests too high (over-provisioning)
   ✅ FIX: requests = typical (80th percentile), not peak

❌ MISTAKE 4: No limits at all
   ✅ FIX: Always set limits to prevent runaway processes

❌ MISTAKE 5: Same resources for all replicas of different apps
   ✅ FIX: Match resources to workload type (static vs API vs DB)

❌ MISTAKE 6: Forgetting to account for multiple containers in pod
   ✅ FIX: Sum all container requests in pod spec

❌ MISTAKE 7: Using M instead of Mi
   ✅ FIX: Always use Mi/Gi (binary units)
```

---

### **4. Real Production Example (Optimization)**
```
BEFORE (Wasted Resources):
───────────────────────────
10 API pods:
  requests: 500m CPU, 512Mi memory (guessed)
  Actual usage: 80m CPU, 150Mi memory
  Wasted per pod: 420m CPU, 362Mi memory
  Total waste: 4200m CPU, 3620Mi memory
  Cost: 3 extra nodes @ $200/mo = $600/mo waste

AFTER (Measured & Optimized):
───────────────────────────
10 API pods:
  requests: 100m CPU, 200Mi memory (measured)
  limits: 300m CPU, 400Mi memory
  Actual usage: 80m CPU, 150Mi memory
  Fits on: 2 nodes instead of 5
  Savings: $600/mo → $240/mo (60% cost reduction!)
```

---

### **5. The Senior Engineer Checklist**
```
Before deploying to production:

□ Measured actual resource usage in staging
□ Set requests to 80th percentile usage
□ Set limits to 2-3x requests (or observed peak)
□ Chose appropriate QoS class:
  □ Guaranteed for databases, critical services
  □ Burstable for most applications
  □ BestEffort only for batch jobs
□ Verified pods will fit on existing nodes
□ Added monitoring/alerts for:
  □ OOMKilled events
  □ CPU throttling
  □ Pending pods
□ Documented why these specific values were chosen
```

---

## 🎓 DAY 13-14 COMPLETE SUMMARY

### **What You Mastered:**

✅ **Core Concepts:**
- requests vs limits (scheduling vs enforcement)
- CPU units (millicores) and memory units (Mi/Gi)
- QoS classes (Guaranteed, Burstable, BestEffort)

✅ **Workload Patterns:**
- Static content: moderate CPU, low memory
- API processing: balanced both
- Data storage: low CPU, high memory
- Computation: high CPU, low memory

✅ **Practical Skills:**
- Measure actual usage with kubectl top
- Write deployments with resources from memory
- Diagnose OOMKilled and Pending pods
- Calculate if pods fit on nodes
- Understand cost impact of optimization

✅ **Production Readiness:**
- When to use each QoS class
- How to monitor resource usage
- When to adjust resources
- Common mistakes to avoid

---

### **Assessment Score: 94%**
- Strong understanding of concepts ✅
- Can write production configs ✅
- Minor gap: requests = typical (not minimum) ⚠️
- Interview ready on resources topic ✅

---

### **Interview Questions You Can Answer:**

1. ✅ "Explain requests vs limits"
2. ✅ "Pod stuck Pending, how to debug?"
3. ✅ "Pod keeps getting OOMKilled, what do you check?"
4. ✅ "What are QoS classes and why do they matter?"
5. ✅ "How do you determine resource requirements?"
6. ✅ "What's the cost impact of over-provisioning?"

---

## 🚀 NEXT STEPS:

**Immediate (Next 24 hours):**
```
□ Review Q4 & Q5 (requests = typical, Redis = memory constraint)
□ Practice writing 3 more deployments from memory
□ Run one more chaos test (your choice: OOMKill or Pending)
```
```

**Production Application:**
```
□ Audit existing deployments (if you have access)
□ Identify over-provisioned workloads
□ Calculate potential cost savings
□ Present findings to team