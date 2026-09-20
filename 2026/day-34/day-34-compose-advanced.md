# Day 34 – Docker Compose: Real-World Multi-Container Apps


### Task 1: Build Your Own App Stack
Create a `docker-compose.yml` for a 3-service stack:
- A **web app** (use Python Flask, Node.js, or any language you know)
- A **database** (Postgres or MySQL)
- A **cache** (Redis)

Write a simple Dockerfile for the web app. The app doesn't need to be complex — even a "Hello World" that connects to the database is enough.

[App-file](2026/day-34/flask-mysql-redis-app)

---

### Task 2: depends_on & Healthchecks
1. Add `depends_on` to your compose file so the app starts **after** the database
2. Add a **healthcheck** on the database service
3. Use `depends_on` with `condition: service_healthy` so the app waits for the database to be truly ready, not just started

**Test:** Bring everything down and up — does the app wait for the DB?
  - yes
  - web app wait for database to start first.

![Task-2.3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-34/Images/Task.2-3.png)

[docker-compose](2026/day-34/flask-mysql-redis-app/docker-compose.yml)

---

### Task 3: Restart Policies
1. Add `restart: always` to your database service
2. Manually kill the database container — does it come back?
3. Try `restart: on-failure` — how is it different?
4. Write in your notes: When would you use each restart policy?
  - restart: always - Docker restarts the container no matter why it stopped. The only way to stop it from restarting is to explicitly `run docker stop or docker compose down`  
    Use when : 	Long-running services that should never be "down"
- restart: on-failure - Docker restarts the container only if it exits with an error (a non-zero exit code).  
  Use When: Data processing jobs One-time migration scripts
---

### Task 4: Custom Dockerfiles in Compose
1. Instead of using a pre-built image for your app, use `build:` in your compose file to build from a Dockerfile
2. Make a code change in your app
3. Rebuild and restart with one command

[Dockerfile](2026/day-34/flask-mysql-redis-app/Dockerfile)

[docker-compose](2026/day-34/flask-mysql-redis-app/docker-compose.yml)

![web-app](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-34/Images/web-app.png)

---

### Task 5: Named Networks & Volumes
1. Define **explicit networks** in your compose file instead of relying on the default
2. Define **named volumes** for database data
3. Add **labels** to your services for better organization

[compose](2026/day-34/flask-mysql-redis-app/docker-compose.yml)

---

### Task 6: Scaling (Bonus)
1. Try scaling your web app to 3 replicas using `docker compose up --scale`
2. What happens? What breaks?
3. Write in your notes: Why doesn't simple scaling work with port mapping?

![scalling](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-34/Images/task.6.png)

- First container started
- It binds host port 5000 = container port 5000.
- Second and third containers failed
- Status Created means Docker couldn’t start them,port 5000 is already in use on the host.
- Docker can’t bind multiple containers to the same host port.
  
---


