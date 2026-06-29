# Day 03 – Linux Commands Practice

## Process management
1. `Ps aux` -To take a snapshot of all the running proccess in your system
2. `top & htop` - Shows realtime data of all the runnning proccess
3. `pgrep <process-name>` - to check PID of any particular proccess
4. `kill <PID>` - to kill the ptocess
5. `kill -9 <PID>` - Forcefully kill the proccess
6. `pkill <process-name>` -kill the process by name
   
## File system
1. `touch` -create an empty file
2. `pwd` - to check current working directory
3. `ls` - to list all the file and directory
4. `cat` - display the content of the file
5. `top X` -display last 10 line of file X
6. `tail X` - display last 10 line of file X
7. `mkdir X` - create a new directory
8. `cp source dest` - copy file
9. `mv source dest` - move the file
10. `chmod 777 X` - chnage the file permission
11. `grep pattern /file` - to fine the text pattern
    
## Networking troubleshooting
1. `ifconfig` - Display all network interfaces with IP addresses.
2. `netstat -a` - Show listening tcp and udp ports and corresponding programs.
3. `traceroute host` - Traces network path.
4. `wget url` - Download files from internet.
5. `whois domain` - Displays whois information for domain.
6. `host domain` - Displays DNS IP address for domain.
7. `nslookup domain` - Display IP address of domain.
8. `ping domain` - check network connectivity


