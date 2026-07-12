# Day 04 – Linux Practice: Processes and Services  
Practicing Linux proccess, Service and analysing the log

## Process command
- List starting 10 lines of the proccess  
`Ps aux | head `

**Result**

![snapshot](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/ps-aux.jpg)

- Find the proccess by the username  
`ps -u root | head -5 ` - list the proccess owned by the root user

**Result**

![snapshot](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/ps-u.jpg)

## Service command

- List starting 10 lines of the running services  
`systemctl list-units --type=service --state=running | head`

**Result**

![systemctl](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/systemctl.jpg)

- Check the status of any service  
 `systemctl status nginx`   Find out if nginx service is running or not

**Result**
![Nginx](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/Nginx.jpg)


## Log Command

- Check the logs of linux services  
`journalctl -u nginx |tail -10 `  Display logs for nginx service

**Result**
![journalctl](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/journalctl.jpg)

- tail -n 25 /var/log/auth.log - Last 25 lines of the authentication log(ssh, sudo).

**Result**

![auth-log](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-04/auth-log.jpg)
