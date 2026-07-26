# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

## Task 1: DNS – How Names Become IPs  
**Answer**

    1- First the browser checks in local cache for the corresponding IP address.
    If not present browser will send request to DNS(Domain Name Service) requesting IP address.
    
    2- Computer sets up a secure connection (HTTPS) with Google’s servers using TCP/IP.
    
    4- The request is routed through Google’s load balancers to the right web server.
    
    4- The web server processes the request, may talk to application servers and databases, 
    and then sends back the webpage you see.

- what happens when you type `google.com` in a browser?  
     
- What are DNS record types?  
  A DNS record is just a piece of information stored in the Domain Name System
  1. A Record : Resolve the domain name into ipv4 address. Domain → ipv4.
  2. AAAA Record : resolve the domain name to ipv6 address.
  3. Cname Record : Another domain name. Helps to manage multiple subdomain.
  4. MX Record : Mail server hostname (+priority). Where to send mail of the domain.
  5. NS record : Authoritative DNS server hostname. Who manages this domain's DNS

- Run: dig google.com — identify the A record and TTL (Time to leave)  from the output.  
  TTL = 164 Seconds
  
  ![TTL](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-15/Images/Dig-%20A.jpg)

  --------

## Task 2: IP Addressing

- What is an IPv4 address? How is it structured? (e.g., 192.168.1.10)  
  IPV4 is identity of network device or host in a network.  
  An IPv4 address has 4 numbers (octets) separated by dots. Each octet is 8 bits, ranging from 0 to 255.  
  Total = 32 bits = 4 × 8 bits.

  ```bash
  192.168.1.10  →  11000000.10101000.00000001.00001010
  ```
  
- Difference between public and private IPs — give one example of each.
  
**Public IP**                                           |   **Private IP**
--------------------------------------------------------|--------------------------------------------------------------------
It is assigned by ISP to every device on the internet.  |   Assigned within private networks to identify devices  locally. 
It is unique across the entire internet.                |   Not routable on the internet.
Example: `103.176.157.29`, `8.8.8.8 (Google DNS)`       |   Example: `192.168.x.x`, `10.x.x.x`,`172.16.x.x`


- What are the private IP ranges?
   - `10.x.x.x` - Large enterprise networks  
   - `172.16.x.x – 172.31.x.x` - Medium-sized organizations  
   - `192.168.x.x` - Home & small office network  
     
- Run: ip addr show — identify which of your IPs are private
  Private ip of my linux system : 10.0.2.15

  ![ip-addr](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-15/Images/ip-addr.jpg)

  ---------------

## Task 3: CIDR & Subnetting

1. What does `/24` mean in `192.168.1.0/24`?  
   Out of 32 bits of IPV4 addess 24 are reserve for network and 8 are reserve for host.  
   1. Total number of IP address : 2<sup>32-24=8</sup> = 256
   2. No. of IP address available for use = 254
   3. Subnet mask = 255.255.255.0
   
3. How many usable hosts in a `/24`? A `/16`? A `/28`?
   
   | CIDR | Total IP | N0. of Usable Ip address |
   | ---- |  ------  |  -----------    |
   | /24  |  256     |  254    |
   |  /16 |  65,536  | 65,534  |
   | /28  |  16      |  14    |

4. Explain in your own words: why do we subnet?  
   Subnet is dividing a large network in to small network so that we can manage it efficently and make it more secure and keep an eyes on the traffic flow.
   
6. Quick exercise — fill in:

| CIDR | Subnet Mask | Total IPs | Usable Hosts |
|------|-------------|-----------|--------------|
| /24  | 255.255.255.0 | 256     | 254          |
| /16  | 255.255.0.0  |  65,536  | 65,534       |
| /28  | 255.255.255.240 | 16      | 14       |

------------

## Task 4: Ports – The Doors to Services
1. What is a port? Why do we need them?
   A port number is part of the addressing information in TCP/IP.It works together with an IP address to direct traffic to the right application.
   A computer is running multiple Apps so port number decide whis apps made the request
   
3. Document these common ports:

| Port | Service |
|------|---------|
| 22   | SSH     |
| 80   | HTTP    |
| 443  | HTTPS   |
| 53   | DNS     |
| 3306 | MySQL DB   |
| 6379 | Redis   |
| 27017| MongoDB |

3. Run `ss -tulpn` — match at least 2 listening ports to their services
   Port 22 is listening → Service : SSH
   Port 53 is listening → Service : DNS

   ![Port](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-15/Images/SS-tulnp.jpg)

-------------

## Task 5: Putting It Together  
- When you run `curl http://localhost:80`
   * Protocol HTTP
   * Localhost : Resolve to loopback IP it resolves to 127.0.0.1
   * Port 80 : Apache service 
   
- Your app can't reach a database at `10.0.1.50:3306` — what would you check first?
   * `ss -tulpn | grep 3306` - Check if port is open and service is listening.
   * `systemctl status mysql` - Check service status
   * `nc -zv 10.0.1.50 3306` - Check connectivity
   * `journalctl -u mysql` - Check Logs

