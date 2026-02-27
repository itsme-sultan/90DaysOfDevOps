# Day 29 – Introduction to Docker

## Task
Today's goal is to **understand what Docker is and run your first container**.

You will:
- Learn why containers exist and how they differ from VMs
- Install Docker on your machine
- Run and explore containers from Docker Hub

---

## Expected Output
- A markdown file: `day-29-docker-basics.md`
- Screenshots of your running containers

---

## Challenge Tasks

### Task 1: What is Docker?
-Docker is a platform for building, running, and managing containers.  
-A container is a lightweight, portable package that includes everything needed to run an application: the code, dependencies, libraries, and configuration.  
-Why we need container :  
Imagin a situation where devolper devlop a code and it runs in his machine however client said its not ruuning in mine. It happened because of environemnt defference, different os, different version.  
To solve this issue we need containerso sp that we have can smilar environment and our codr run without failur.
- Containers vs Virtual Machines — what's the real difference?  
  VM need allocation of the resource that means we need to dedicated hardware while container use shared resource and once we delete the container all resources is free and available for the use.
- What is the Docker architecture? (daemon, client, images, containers, registry)

Draw or describe the Docker architecture in your own words.  
-Docker Client -thorugh this we interact with docker like CLI opr docker deksptop app  
-Docker Engine  
-Docker Daemon  - Brain of the container --> it create images, run container, manager network & volume.- Runs in the background.
-Docker Registry  -Store the docker Image --> Privet & public -->doker hub is example of public registry

---

### Task 2: Install Docker
1. Install Docker on your machine (or use a cloud instance)
2. Verify the installation
3. Run the `hello-world` container
4. Read the output carefully — it explains what just happened

---

### Task 3: Run Real Containers
1. Run an **Nginx** container and access it in your browser
2. Run an **Ubuntu** container in interactive mode — explore it like a mini Linux machine
3. List all running containers
4. List all containers (including stopped ones)
5. Stop and remove a container

---

### Task 4: Explore
1. Run a container in **detached mode** — what's different?
2. Give a container a custom **name**
3. Map a **port** from the container to your host
4. Check **logs** of a running container
5. Run a command **inside** a running container

---

## Hints
- `docker run`, `docker ps`, `docker stop`, `docker rm`
- Interactive mode: `-it` flag
- Detached mode: `-d` flag
- Port mapping: `-p host:container`
- Naming: `--name`
- Logs: `docker logs`
- Exec into container: `docker exec`

---

## Why This Matters for DevOps
Docker is the foundation of modern deployment. Every CI/CD pipeline, Kubernetes cluster, and microservice architecture starts with containers. Today you took the first step.

---

## Submission
1. Add your `day-29-docker-basics.md` to `2026/day-29/`
2. Commit and push to your fork

---

## Learn in Public
Share your first Docker container screenshot on LinkedIn.

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
