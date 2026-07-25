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
  ![ip-addr]()
  
- Reachability: ping <google.com>
  Observation : No packet loss, Average latency is 2.3 ms shows low latency.

  ![ping]()
  
- Path: traceroute <target> (or tracepath) — note any long hops/timeouts.
  Observation :
  
Ports: ss -tulpn (or netstat -tulpn) — list one listening service and its port.
Name resolution: dig <domain> or nslookup <domain> — record the resolved IP.
HTTP check: curl -I <http/https-url> — note the HTTP status code.
Connections snapshot: netstat -an | head — count ESTABLISHED vs LISTEN (rough).
