# Day 14 – Networking Fundamentals & Hands-on Checks

## OSI vs TCP/IP models

**OSI Model** :
| OSI Layer No. (7) | OSI Layer name   | TCP/IP  Layer   | Device/Protocol |
| ------------   | --------      | -----------      | ---------------  |
| Layer 7        | Application   |   Applicatio   | HTTP, HTTPS, FTP, SMTP, DNS |
| Layer 6        | Presentation  |  Application  | SSL/TLS, Encryption, Compression |
| Layer 5        | Session       | Application  |Session Management |
| Layer 4        | Transport     | Transport    |  TCP, UDP ,ARP, Port No.    |
| Layer 3        | Network       |   Internet   |   Router, IP, ICMP  |
| Layer 2        | Data Link     |   Network/Link  | MAC, NIC, Switch, Bridges    |
| Layer 1        | Physical Layer|  Network/Link    | Ethernet cable, Repeater, Hub, Wifi  |


---------------------------

### One real example: “curl https://example.com = App layer over TCP over IP”

- Layer 7: Application Layer → curl make a request to example.com using https protocal.
- Layer 6: Presentation Layer → Encrypts the data with SSL/TLS.
- Layer 5: Session Layer → Establish the session with remote server.
- Layer 4: Transport layer → Remote server start sending respone by securing the data using TCP.
- Layer 3: Network layer  → End to end delivery of data. (src IP → dest IP )
- Layer 2: Data Link Layer → Hop to Hop delivery, MAc address is added for local routing.
- Layer 1 : Physical Layer →  Data conver into electrical signals.Data tansfer in bits.

---------------------------------------------------

## Hands-on Checklist

- Identity: hostname -I (or ip addr show)  
  Observation : Local Ip address of EC2 instance is 172.31.47.23.
  
  ![ip-addr](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/ip-addr.jpg)
  
- Reachability: ping <google.com>  
  Observation : No packet loss, Average latency is 2.3 ms shows low latency.

  ![ping](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/Ping.jpg)
  
- Path: traceroute <google.com>  
  Observation : Reach the destination successfully with 17 hops. No repsonse for hp 10-16 due to security.

  ![Traceroute](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/traceroutr.jpg)
  
- Ports: ss -tulpn (or netstat -tulpn) — list one listening service and its port.  
  Observation : Port 20 & 80 is listening. means ready to accesspt SSH & hhtp connection.

  ![netsta](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/netstat.jpg)
  
- Name resolution: dig <google.com> or nslookup <domain>  
  Observation : Google have 6 ipv4 ip address.

  ![dig](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/dig.jpg)
  
- HTTP check: curl -I google.com
  Obervation : HTTP Status code is 301 Moved Permanently. Always redirect to http://www.google.com/

  ![curl](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/curl.jpg)

- Connections snapshot: netstat -an | head  
  Observation: Two established connection on port 22 and many ports arev  listening.

  ![netstat-an](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/netstat-az.jpg)

  -------------------

## Mini Task: Port Probe & Interpret

- Identify one listening port from `ss -tulpn`.
- From the same machine, test it: nc -zv localhost <port> (or curl -I http://localhost:<port>).
  Observation: Localhost successfly connected to port 22.

  ![localhost](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-14/Images/netcat.jpg)
  
- If service is not reachable, check the service status `systemctl status ssh` or firewall rules.

- -----------------
## Reflection
- Which command gives you the fastest signal when something is broken? -  `ping `
- What layer (OSI/TCP-IP) would you inspect next,
- if DNS fails?
  - OSI : Application Layer
  - TCP\IP : Application layer
  - Reason:
    1. DNS is application layer protocol
    2. Issue is with DNS Resolver.
  
- If HTTP 500 shows up?
  - OSI : Application layer
  - TCP\IP : Application Layer.
    Reason:
    1. Request reacched the server, connection stablished.
    2. Issue is with server side.
       
- Two follow-up checks you’d run in a real incident.
- IF DNS fails?
  ``` bash
  ping <ip>
  dig <dns>
  ```

- If HTTP 500 shows up?
  ``` bash
  traceroute <dns>
  cutl -I <dns>
  ```
  












