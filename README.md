# docker-k8s-project


## 📋 PART 1: Why Docker Compose? (The Problem)

**Remember your Day 1 project?** You built a 3-tier web application. Let me show you what you had to do:

```bash
# Create network
docker network create my-network

# Start database
docker run -d --name db --network my-network -e POSTGRES_PASSWORD=secret postgres

# Start backend
docker run -d --name backend --network my-network my-backend-image

# Start frontend
docker run -d --name frontend --network my-network -p 80:80 my-frontend-image
```

**Problems with this approach:**
1. ❌ Too many manual commands
2. ❌ Hard to remember all the flags
3. ❌ No easy way to start/stop everything together
4. ❌ Configuration scattered across multiple commands
5. ❌ Difficult to share with team (how do they know what commands to run?)

---

## 🎯 Docker Compose = Solution!

**Docker Compose** lets you define ALL of this in **ONE YAML file** and manage with **ONE command**!

```bash
# Instead of 4+ commands, just:
docker-compose up
```

**Benefits:**
- ✅ All configuration in one file (`docker-compose.yml`)
- ✅ Start everything: `docker-compose up`
- ✅ Stop everything: `docker-compose down`
- ✅ Easy to share with team (just share the file!)
- ✅ Version control the entire setup
- ✅ Reproducible on any machine

---

## 📝 HANDS-ON: Your First docker-compose.yml

Let's start simple. Create a directory and your first compose file:

**Command 1:**
```bash
cd ~
mkdir compose-demo
cd compose-demo
```

**Command 2:** Create a basic `docker-compose.yml` file:
```bash
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
EOF
```

**Command 3:** Start it!
```bash
docker-compose up
```

---

**Execute these 3 commands and share the output!** 

You should see Docker Compose:
1. Creating a network automatically
2. Starting the nginx container
3. Logs streaming in real-time

