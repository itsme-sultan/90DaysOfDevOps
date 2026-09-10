# Day 31 – Dockerfile: Build Your Own Images

### Task 1: Your First Dockerfile
1. Create a folder called `my-first-image`
2. Inside it, create a `Dockerfile` that:
   - Uses `ubuntu` as the base image
   - Installs `curl`
   - Sets a default command to print `"Hello from my custom image!"`
3. Build the image and tag it `my-ubuntu:v1`
4. Run a container from your image

**Verify:** The message prints on `docker run`

![Task1.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.1-1.png)
![Task.1-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.1-2.png)

---

### Task 2: Dockerfile Instructions
Create a new Dockerfile that uses **all** of these instructions:
- `FROM` — base image
- `RUN` — execute commands during build
- `COPY` — copy files from host to image
- `WORKDIR` — set working directory
- `EXPOSE` — document the port
- `CMD` — default command

Build and run it. Understand what each line does.

![Task.2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.2.png)
---

### Task 3: CMD vs ENTRYPOINT
1. Create an image with `CMD ["echo", "hello"]` — run it, then run it with a custom command. What happens?
  - When you run the container with a custom command (e.g., echo "custom command"), the custom command completely overrides the CMD

![Task.3-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Tssk.3-1.png)

2. Create an image with `ENTRYPOINT ["echo"]` — run it, then run it with additional arguments. What happens?
- Run without arguments: The container runs echo with no arguments,resulting in a blank line (no output).
- Run with additional arguments: When you pass arguments (e.g., hello-world), they are appended to the ENTRYPOINT, so it runs echo hello-world and outputs:

![Task.3-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.3-2.png)

3. Write in your notes: When would you use CMD vs ENTRYPOINT?
  - Use CMD when you want to provide a default command that can be changed easily when you run the container.
  - Use ENTRYPOINT when you want to set a fixed command that always runs.

---

### Task 4: Build a Simple Web App Image
1. Create a small static HTML file (`index.html`) with any content
2. Write a Dockerfile that:
   - Uses `nginx:alpine` as base
   - Copies your `index.html` to the Nginx web directory
3. Build and tag it `my-website:v1`
4. Run it with port mapping and access it in your browser
   
   ```bash
   FROM nginx:alpine
   WORKDIR /app
   COPY index.html usr/share/hginx/html
   EXPOSE 80
   ```

![Task.4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.4.png)

---

### Task 5: .dockerignore
1. Create a `.dockerignore` file in one of your project folders
2. Add entries for: `node_modules`, `.git`, `*.md`, `.env`
3. Build the image — verify that ignored files are not included

![Task.5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.5.png)

-Verified there is no `node_modules`, `.git`, `*.md`, `.env` copied in the container.

---

### Task 6: Build Optimization

1. Build an image, then change one line and rebuild — notice how Docker uses **cache**

```bash
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]
```
Observation: The image is built successfully and all layers are created.

Change one line and rebuild: Added Port & changed app.py

```bash
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","app.py"]
```

Observation:
Even though only the application code changed
Docker re-ran pip install -r requirements.txt
Any change in Dockerfile  invalidated the cache for all following layers.



2. Reorder your Dockerfile so that frequently changing lines come **last**

```bash
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","app.py"]
```

![image](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-31/Images/Task.6-2.png)

Observation:
Docker reused cached layers for: Base image,Working directory,Dependency installation

3. Why does layer order matter for build speed?

- Docker builds images in layers and caches each layer.
- If a layer changes,Docker rebuilds that layer and all layers after it.
- By placing:
    - Rarely changing files (dependencies) first
    - Frequently changing files (source code) last
- Docker can reuse cached layers,resulting in faster rebuilds.

---
