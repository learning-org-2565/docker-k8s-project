FOCUS ON:
✅ WHY services need different resources
✅ HOW to observe which service struggles
✅ WHAT happens when you scale struggling services
✅ THE EVIDENCE (metrics, load tests, visual proof)

DON'T FOCUS YET:
❌ Every line of Python code
❌ Deep Flask framework details
❌ Prometheus query language
❌ Grafana dashboard customization


CRITICAL OBSERVATIONS:
1. Response times (fast vs slow services) the payamnt is slow observer, product is fast so quick time
2. CPU usage (which service maxes out?) which service taking more cpu for service loading
3. Request throughput (requests/second) how many quests it is taking for sec
4. Success vs failure rate which one is failing why?
5. Effect of scaling (1 instance → 5 instances) if the load is coming it should be replicate

UNDERSTAND:
✅ Volumes (we'll clarify this NOW!)
✅ docker-compose scale command - vry imp
✅ Resource limits (CPU, memory) 
✅ Networking between containers

DON'T NEED TO MASTER:
❌ Building custom images (we're using base images + volumes)
❌ Advanced Dockerfile optimization
❌ Multi-stage builds (Day 2 stuff)

80% of learning comes from:
- Running the project ✅
- Observing the results ✅
- Breaking things and fixing them ✅
- Load testing and scaling ✅

20% of learning comes from:
- Understanding every line of code ❌
- Knowing all tool options ❌
- Perfect configuration ❌