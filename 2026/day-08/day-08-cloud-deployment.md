# Day 08 – Cloud Server Setup: Docker, Nginx & Web Deployment

## Part 1: Launch Cloud Instance & SSH Access  
Step 1: Created a Ubuntu EC2 Instance in AWS account  

Step 2: Connect via SSH  
- Setup the security group for SSH connection (Port 22)  
- Access the AWS EC2 instance from local system using Git bash terminal  
  `ssh -i "private-key.pem" username@public-ip/hostname`

![Ec2-instance](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-08/Ec2-instance.jpg)

-----

## Part 2: Install Docker & Nginx  
Step 1: Update System  
`sudo apt update && sudo apt upgrade -y`

Step 2: Install Nginx
```
sudo apt install nginx
systemctl start nginx
systemctl enable nginx
```

Step 3: Install docker
```
sudo apt install docker.io
systemctl start dokcer
systemctl enable docker
```

---------

## Part 3: Security Group Configuration
- Setup the security group fot http traffic (Port 80)  
- Test Web Access: Open browser and visit: http://<instance-ip>

![web-page](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-08/Nginx-webpage.jpg)

------------

## Part 4: Extract Nginx Logs  
Step 1: View Nginx Logs
`journalctl -u nginx`

Step 2: Save Logs to File
`sudo cat /var/log/nginx/access.log > nginx-logs.txt`

Step 3: Download Log File to Your Local Machine  
`scp -i "Mylinux-server.pem" ubuntu@13.232.139.224:/home/ubuntu/nginx-logs.txt ./nginx-logs.txt`

![nginx-log](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-08/nginx-log.jpg)

--------------

## Commands Used  
- ssh -i "private-key.pem" username@public-ip/hostname  
- sudo apt update && sudo apt upgrade -y  
- systemctl status <service>  
- journalctl -u <service>  
- scp -i "Mylinux-server.pem" ubuntu@13.232.139.224:/home/ubuntu/nginx-logs.txt ./nginx-logs.txt  

## What I Learned  
- Unable to access nginx web page, setup the sssercurity group for http traffic  
- Unable to copy the nginx log file in local system used ./nginx-logs.txt instead of .
