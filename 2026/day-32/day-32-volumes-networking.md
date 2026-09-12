# Day 32 – Docker Volumes & Networking

### Task 1: The Problem
1. Run a Postgres or MySQL container

![Task.1-1]()

2. Create some data inside it (a table, a few rows — anything)

![Task.1-2]()

3. Stop and remove the container
4. Run a new one — is your data still there?

![Task.1-4]()

- No, Data is lost when a container is removed because containers are ephemeral and do not persist data by default.

---

### Task 2: Named Volumes
1. Create a named volume
![Task.2-1]()

2. Run the same database container, but this time **attach the volume** to it
![task.2-3]()

3. Add some data, stop and remove the container
![Task.2-3 a]()  
![Task.2-3 b]()

4. Run a brand new container with the **same volume**
![Task.2-4]()

5. Is the data still there?
 - Yes, all the table and row are intact. data persisted by attaching the docker volume.

**Verify:** `docker volume ls`, `docker volume inspect`

![Task.2-6]()

---

### Task 3: Bind Mounts
1. Create a folder on your host machine with an `index.html` file
2. Run an Nginx container and **bind mount** your folder to the Nginx web directory
3. Access the page in your browser
![Task.3-1]()

4. Edit the `index.html` on your host — refresh the browser
![Task.3-2]()

Write in your notes: What is the difference between a named volume and a bind mount?
- Named Volume :
  1. Created and managed by Docker
  2. Stored under Docker’s internal path: /var/lib/docker/volumes/...
  3. Best for persistent data where you don’t care about the exact host path.

- Bind Volume
  1. Maps a specific host directory into the container.  
     ` docker run -v /home/sultan/mysql_data:/var/lib/mysql mysql`
  2. You control the exact path on your host machine.

---

### Task 4: Docker Networking Basics
1. List all Docker networks on your machine
2. Inspect the default `bridge` network
![task.4-2]()

3. Run two containers on the default bridge — can they ping each other by **name**?
 - No, On the default bridge network, Docker does not provide automatic DNS resolution between containers.
![Task.4-3]()

4. Run two containers on the default bridge — can they ping each other by **IP**?
   - Yes, can ping by the ip address.

 ![Task.4-4]()

---

### Task 5: Custom Networks
1. Create a custom bridge network called `my-app-net`
![Task.5-1]()

2. Run two containers on `my-app-net`
3. Can they ping each other by **name** now?
![Task.5-3]()

4. Write in your notes: Why does custom networking allow name-based communication but the default bridge doesn't?  
   - Default Docker bridge network does not have built-in DNS,so containers cannot resolve each other by name.they need IPs.
   - User-defined networks have **embedded DNS**, so containers can communicate using their names.
---

### Task 6: Put It Together
1. Create a custom network
2. Run a **database container** (MySQL/Postgres) on that network with a volume for data
3. Run an **app container** (use any image) on the same network
4. Verify the app container can reach the database by container name

![Task.6]()

---
