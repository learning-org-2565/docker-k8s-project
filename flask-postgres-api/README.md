sed (Stream Editor) command is a command line  unitility to replace the text during the command execution
-i inplace
s:/ substitution command
ex: sed -i "s/ db:/ database:/" docker compose.yaml
sudo iptables -t nat -L DOCKER -n -v --line-numbers | grep 5000
3        0     0 DNAT       tcp  --  !br-0ba5585fc989 *       0.0.0.0/0            0.0.0.0/0            tcp dpt:5000 to:172.18.0.3:5000

1. What:
"Built a 2-tier Flask API + PostgreSQL stack using Docker Compose with health checks, resource limits, and DNS-based service discovery."
2. Why:
"Demonstrates production container orchestration where services communicate by DNS names not IPs - the same pattern K8s uses for pod-to-pod communication and horizontal scaling."
3. Concrete Example:
"Deployed 2 services in under 10 minutes with automated health checks validating database connectivity; when issues occur, Docker marks containers unhealthy while K8s would auto-restart them for zero-downtime recovery."

