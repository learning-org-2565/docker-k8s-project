sudo iptables -t nat -L DOCKER -n -v --line-numbers | grep 5000
3        0     0 DNAT       tcp  --  !br-0ba5585fc989 *       0.0.0.0/0            0.0.0.0/0            tcp dpt:5000 to:172.18.0.3:5000
[ec2-user@ip-172-31-23-213 flask-postgres-api]$ 

