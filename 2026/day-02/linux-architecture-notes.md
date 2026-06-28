# Linux Architecture, Processes, and systemd

## The core components of Linux  
1 -**Kernel (The Core)**  
Role: Manages CPU, memory, devices, and processes. Acts as a bridge between hardware and software.

Functions:  
Process management: Schedules tasks fairly.  
Memory management: Allocates RAM efficiently.  
Device drivers: Controls hardware like disks, network cards.  
Security: Enforces permissions and access control.  

2 -**Shell (The Interface)**  
Role: Command-line interpreter that lets users talk to the OS.  
Types: Bash, Zsh, Fish.  
Functions: Executes commands, scripts, and automates tasks  

3 -**System Libraries**  
System libraries are pre-written collections of code (.so files — "shared objects") stored mainly in /lib, /lib64, and /usr/lib. 

Role: Provide reusable functions that applications use to interact with the kernel.  
Example: The GNU C Library (glibc) offers functions like printf() or file handling.  
Usage: When you run a program, it calls library functions instead of directly talking to the kernel.  
Example: ls uses system libraries to request file info from the kernel.  

4 -**System Utilities**  
They are built on top of system libraries. utilities borrow code from libraries.  
Role: Essential tools for system management and user tasks.  
Examples:cp, ps, df -h etc

Tip: These utilities are stored in directories like /bin, /sbin, /usr/bin.


## How processes are created and managed
- When you run any program, Linux creates a process for it. A process is simply a running instance of a program with its own memory, resources, and identity.  
- Every process gets a unique PID (Process ID) — a number Linux uses to track it.  
- ps aux, top -->use to check running programme  
- Kill , kill -9 -->use to stop the proccess  

Process State :  
* Running (R) -Process is actively using the CPU right now.  
* Stopped (T) - Process is paused/frozen. Happens when you press Ctrl+Z in terminal  
* Zombie (Z)- Process has finished but its parent hasn't acknowledged it yet. Takes no CPU or RAM — just occupies a PID  

## What systemd does and why it matters
When Linux boots, the kernel starts first. After that, the kernel needs someone to start everything else — all services, processes, and your desktop.  
That "someone" is called Init. systemd is the modern init system most distros use today.  
Init = Process ID 1 = The Mother of all Processes  
Every single process on your Linux system is a child of Init

`systemctl` = service management  
`journalctl`= Systemd's Logging System

## 5 Linux command I use on daily basis
* ls - to lis the file  
* ps - to see the sanpshot of all the running proccess  
* ssh - to connect remote serveer  
* df -h - to check disk space  
* chmod - to change the file/directory permission  




Happy Learning  
**TrainWithShubham**
