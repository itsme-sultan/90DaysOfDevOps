## Runbook for SSH Service

## Environment basics

 1. command : `uname -a `
    **Output** : `Linux ip-172-31-47-23 7.0.0-1008-aws #8-Ubuntu SMP PREEMPT Fri Jun 19 00:15:35 UTC 2026 x86_64 GNU/Linux`  
    **Observation** : Listed the details of system’s kernel and operating environment.

2. Cpmmad: ` cat /etc/os-release `
   **Output** : `Ubuntu 26.04 LTS`
   **Observation** : Checked which Linux distribution and version is running

## CPU & Memory utilization  

 1. Command**: `ps -o pid,pcpu,pmem,comm -C sshd`


