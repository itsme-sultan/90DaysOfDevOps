## Runbook for SSH Service

## Environment basics

 1. command : `uname -a `  
    **Output** : `Linux ip-172-31-47-23 7.0.0-1008-aws #8-Ubuntu SMP PREEMPT Fri Jun 19 00:15:35 UTC 2026 x86_64 GNU/Linux`  
    **Observation** : Listed the details of system’s kernel and operating environment.

2. Commad: ` cat /etc/os-release `  
   **Output** : `Ubuntu 26.04 LTS`
   **Observation** : Checked which Linux distribution and version is running

## CPU & Memory utilization  

 1. **Command**: `ps -o pid,pcpu,pmem,comm -C sshd`  
    **Output** :  
     ```
    PID %CPU %MEM COMMAND
    982  0.0  0.8 sshd
    ```
     **Observation** : Daemon PID is 982. CPU utilization is 0.

 2. **Command** : `free -h`  
    **Output** :
```
               total        used        free      shared  buff/cache   available
Mem:           908Mi       369Mi       200Mi       2.8Mi       447Mi       538Mi
Swap:             0B          0B          0B

```
   **Observation** : Check the memoty utilization. 538 mb memory is free.

## Disk / IO

1. **Command** : `df -h`  
   **Output** :
   
   ![snapshot](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-05/Disk-utilization.jpg)

   **Observation** : There is only one disk is mounted. 34% disk is in use.

2. **Command** : `sudo du -sh /var/log`  
   **Output** : ` 19M     /var/log `  
   **Observation** : Size of log directory is 19M.

## Network

1. **Command** : `ss -tulnp | grep 22 `  
   **Output** :
   ```
   tcp   LISTEN 0      4096             0.0.0.0:22         0.0.0.0:*
   tcp   LISTEN 0      4096                [::]:22            [::]:*
   ```

   **Observation** : Port 22 is open and listening.

2. **Command** : `curl -I https://example.com`  
   **Output** :
   ```
   HTTP/1.1 200 OK
   Date: Tue, 14 Jul 2026 17:20:00 GMT
   Server: Apache/2.4.41 (Ubuntu)
   Content-Type: text/html; charset=UTF-8
   Content-Length: 1256
   ```
   **Observation** : Site is up and running.

## Logs
1. **Command** : `journalctl -u ssh -n 20`  
   **Output** :
   
   ![ssh](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-05/SSH.jpg)

   **Observation** :  Recent login attempts record. No suspicious activity detected.

## If this worsens (next steps)

1. Will check the disk utilization.
2. find the proccess with hight cpu utilization
3. kill the high cpu utilization proccess
4. if ssh failed to connect will check port 22 listenong




    


