# Day 29 – Introduction to Docker

### Task 1: What is Docker?
- Docker is a platform for building, running, and managing containers.  
- A container is a lightweight, portable package that includes everything needed to run an application: the code, dependencies, libraries, and configuration. 

### Why we need container :  
- Imagin a situation where devolper devlop a code and it runs in his machine however client said its not ruuning in mine. It happened because of environemnt defference, different os, different version.  
- To solve this issue we need containerso so that we have smilar environment and our codr run without failur.  
- You can build locally,deploy to the cloud and run anywhere on any server.

### Containers vs Virtual Machines — what's the real difference?
  * Virtual Machines (VMs): Each VM includes a full guest OS, virtualized hardware, and runs on a hypervisor. Heavy (GBs), slow to boot (minutes).
  * Containers: Share the host machine's OS kernel but isolate the application's processes, filesystem, and network. Lightweight (MBs), boot in seconds.
  
---

### Docker architecture

### 1. Docker Client

### What it is
The Docker client is the command-line interface (CLI) used to interact with Docker. It acts as the command center.

### How it works
You type commands in the Docker client, and it sends those requests to the Docker daemon, which performs the actual work.

### Example Commands
- `docker build`
- `docker run`
- `docker pull`
- `docker push`

---

### 2. Docker Daemon

### What it is
The Docker daemon (`dockerd`) is the background service that manages Docker objects such as images, containers, networks, and volumes.

### How it works
The daemon:
- Listens for Docker API requests from the Docker client
- Builds images
- Runs and manages containers
- Handles networking and storage


---

### 3. Docker Hub

### What it is
Docker Hub is a cloud-based public registry for Docker images.

### How it works
It works like an app store for container images. 

You can:
- **Pull** images created by others
- **Push** your own images

### Usage
When you need an image to create a container, you can pull it from Docker Hub.

---

### 4. Docker Registry

### What it is
A Docker registry is a system that stores and distributes Docker images. Docker Hub is the most popular public registry,but you can also create private registries.

### How it works
Registries:
- Store Docker images
- Allow users to pull images
- Allow users to push images

Private registries are commonly used by companies to securely store internal application images.

<img width="1472" height="520" alt="image" src="https://github.com/user-attachments/assets/5cead501-35af-4b41-86a6-1eb893b71c16" />

The daemon (dockerd) does the real work — building images, running containers, talking to registries. The CLI is just how you send it commands.


---

### Task 2: Install Docker
1. Installed the docker on cloud instance  
   `apt install docker.io`
3. Verify the installation using command
   `
   docker -v`
5. Run the hello-world container using command  
   `
   docker run hello-world`

![Task.2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-29/Images/Task.2.jpg)
   
7. Read the output carefully — it explains what just happened
   - Docker unable to find image locally.
   - Docker pull the `Hello-world` image from the docker hub.
   - Docker created a container of `Hello World`.
   - Container printed the output `Hello from Docker!` and exited

---

### Task 3: Run Real Containers
1. Run an **Nginx** container and access it in your browser
![Task.3-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-29/Images/Task.3-1.png)

2. Run an **Ubuntu** container in interactive mode — explore it like a mini Linux machine
3. List all running containers
4. List all containers (including stopped ones)
5. Stop and remove a container

![task.3-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-29/Images/Task.3-4.png)

---

### Task 4: Explore
1. Run a container in **detached mode** — what's different?
  - Docker starts the container in the background and immediately hands your terminal back, printing just the container ID.
![Task.4-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-29/Images/Task.4-1.jpg)

2. Give a container a custom **name**
3. Map a **port** from the container to your host
4. Check **logs** of a running container
5. Run a command **inside** a running container

![Tassk.4-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-29/Images/Task.4-4.png)
---



Happy Learning!
**TrainWithShubham**
