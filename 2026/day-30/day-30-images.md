# Day 30 – Docker Images & Container Lifecycle

### Task 1: Docker Images
1. Pull the `nginx`, `ubuntu`, and `alpine` images from Docker Hub  
   used command `docker pull nginx` to pull the images from docker likewise for other also.  

![Task.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.1.png)

2. List all images on your machine — note the sizes
3. Compare `ubuntu` vs `alpine` — why is one much smaller?
   - Ubuntu is a full-featured Linux distribution, while Alpine is a minimal distribution optimized for containers.
   - Ubuntu is larger because it includes GNU tools and glibc, whereas Alpine uses BusyBox and musl, making it much smaller.

4. Inspect an image — what information can you see?  

![Task.1-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.1-4.png)

 - Image ID: sha256:05b8cb6...
 - Image Tag: nginx:latest
 - Exposed Port: 80/tcp (HTTP)
 - Environment variable
 - ENTRYPOINT
 - CMD
 - Lables,maintainer
 - 7 layers |Each layer typically corresponds to a step in the Dockerfile

5. Remove an image you no longer need
   - remove nginx image: ` docker rmi nginx`

---

### Task 2: Image Layers
1. Run `docker image history nginx` — what do you see?
   - The command `docker image history <image>` lets you trace how an image was built layer by layer  

![Task.2-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.2-1.png)

2. Each line is a **layer**. Note how some layers show sizes and some show 0B
   - Layers with a size (MB or kB) were created by instructions that modify the filesystem,such as RUN, COPY, or ADD.
   - Layers showing 0B were created by instructions that only change metadata, such as ENV, CMD, EXPOSE, LABEL, or ENTRYPOINT. These do not change the filesystem.

3. Write in your notes: What are layers and why does Docker use them?
   - Each instruction in a Dockerfile (FROM, RUN, COPY, ADD, etc.) creates a new layer.
   - Layers are stacked on top of each other to form the final image.
   - **Why Docker Uses Layers**
     1. Reusability - Common base layers (like ubuntu:20.04) can be shared across many images.
     2. Caching - If a layer hasn’t changed, Docker reuses it. E.g: If you only change index.html, Docker won’t rebuild the apt-get install step.
     3. Efficiency - Layers are immutable and stored once.Multiple containers can run from the same image without duplicating data.
     4. Portability - Layers are distributed separately.When you docker pull, Docker only downloads missing layers.

---

### Task 3: Container Lifecycle
Practice the full lifecycle on one container:
1. **Create** a container (without starting it)
2. **Start** the container
3. **Pause** it and check status
4. **Unpause** it
5. **Stop** it
6. **Restart** it
7. **Kill** it
8. **Remove** it

Check `docker ps -a` after each step — observe the state changes.

![Task.3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.3.png)

---

### Task 4: Working with Running Containers
1. Run an Nginx container in detached mode
2. View its **logs**
3. View **real-time logs** (follow mode)
![Task.4-3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.4-3.png)

4. **Exec** into the container and look around the filesystem
5. Run a single command inside the container without entering it
![Task.4-5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.4-5.png)

6. **Inspect** the container — find its IP address, port mappings, and mounts
   ` docker inspect <id> `

![Task.4-6](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-30/Images/Task.4-6.png)

---

### Task 5: Cleanup
1. Stop all running containers in one command  
   ` docker kill $(docker ps -q) `
2. Remove all stopped containers in one command  
   ` docker system prune `
3. Remove unused images  
   ` docker image prune -a `
4. Check how much disk space Docker is using  
   ` docker system df `
---

