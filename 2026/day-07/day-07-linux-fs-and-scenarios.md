# Linux File System Hierarchy & Scenario-Based Practice  

**Core Directories (Must Know):**
- `/` (root) - The starting point of everything. Every other directory branches off from there. I would use this to get into ;inux root system.
  
- `/home` - User home directories. Where your personal stuff lives, in a folder named after you: `/home/yourname.` . I would use this to list down all the user's home directory.
  
- `/root` - Root user's home directory. The home directory for the root (admin) user — not to be confused with /, the root of the whole tree.  I would use this to store files that only root should acsess.
  
- `/etc` - Configuration files. Almost every program stores its settings here as plain text (e.g. /etc/passwd, /etc/hosts). I would this to customize 
  
- `/var/log` - Log files.  where Linux keeps its logs — records of what the system, kernel, and various services have been doing. If something breaks, this is usually the first place to look.  
   `auth.log` : I would use this to check logs related to authentication.  
   `syslog` : I would use this tview general system and service related logs.
  
- `/tmp` - Temporary files. Scratch space for temporary files. Often wiped on reboot. I would use this to store temporary file.

**Additional Directories (Good to Know):**
- `/bin` - Essential command binaries.  held commands essential for basic system operation, needed even before other filesystems (like /usr) were mounted. Things like ls, cp, mv, cat, bash.
  
- `/usr/bin` - Contains the majority of user command binaries — programs and utilities that regular users and administrators run in daily work. (ex. ls, mkdir, mv) I would use this to look for commands.
  
- `/opt` - Optional third-party software that doesn't follow the standard packaging conventions.


### Hands on Task :
- Use the command `du -sh /var/log/* 2>/dev/null | sort -h | tail -5` to find 5 largest log file
-  checkthe configuration file `/etc/hostname ` to get the hostname
-  lsited all the file and directory in the home directory ` ls -la `

  ![hosstname](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-07/1.jpg)

---------------------------

# Part 2: Scenario-Based Practice

## Scenario 1: Service Not Starting
```
A web application service called 'myapp' failed to start after a server reboot.
What commands would you run to diagnose the issue?
Write at least 4 commands in order.
```
### My Solution (Step by step):
- step 1: check service status
 
  `syatemctl status myapp`
  
  Why this command? It shows if the service is active, failed, or stopped

- step 2 : Check the log

  `Journalctl -u myapp` 

  why this command? To know the last few state of the service.

- step 3: check if service is enqabled

  `systemctl is-enabled myapp`

  Why this command? To know if it will start automatically after reboot  
  What I learned: Always check status first, then investigate based on what you see.

--------------

## Scenario 2: High CPU Usage
```
Your manager reports that the application server is slow.
You SSH into the server. What commands would you run to identify
which process is using high CPU?
```

### My Solution :
- Step 1: check the live proccess
  
  `htop`

  Why this command? to know all the running proccess.

- Step 2: Sort the proccess by cpu utilization

  ` ps aux --sort=-%cpu | head -20 `

  Why this command? THis will sort the proccess in descending order of cpu utilization.  
  What I learned? sort the proccess by high cpu utilization and note the PID.

---------------

## Scenario 3: Finding Service Logs
```
A developer asks: "Where are the logs for the 'docker' service?"
The service is managed by systemd.
What commands would you use?
```

### My Solution :
- Step 1: CHeck the docker services logs.
  
  ` journalctl -u docker | tail -n 50 `

  Why this command? To knoe service logs

- Step 2: Check the live service logs.

  ` journalctl -u docker -f | tail -50 `

  Why this command? Check the service log in realtime

  -----

  ## Scenario 4: File Permissions Issue
  ```
  A script at /home/user/backup.sh is not executing.
  When you run it: ./backup.sh
  You get: "Permission denied"

  What commands would you use to fix this?
  ```

  ### My Solution :
  
- Step 1: Check the file permission

  ` ls -ltr /home/user/backup.sh `

  Why this command? Tp know if file have execute permission or not.

- Step 2: Chnage the file permission

  ` sudo chmod +x /home/user/backup.sh `

  Why this command? Give file execute permission

- Step 3: Run the script

  `./backup.sh or bash backup.sh `

  Why this commsnd? To check file exxecuted successfully or not.  
  What I learned? ALways check file permission before rubbibg script.
  
  
  
  

