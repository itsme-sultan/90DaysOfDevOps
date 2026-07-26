# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

## Task 1: DNS – How Names Become IPs

- what happens when you type `google.com` in a browser?
  1. When you type the `Google.com` in the browser. It check local cache and host file first.
  2. If it fails too find the IP address at local level. Request has been sent to DNS resolver [ Google (8.8.8.8), Cloudflare (1.1.1.1) ]  
  3. DNS resolver send query to `Root Server `.
  4. The resolver does a recursive search: Root Server → TLD Server → Authoritative Name Server, collecting the real IP
  5. The DNS Resolver returns the final IP to the computer and Google page reflect on the computer screen.
     
- What are these record types?  
  A DNS record is just a piece of information stored in the Domain Name System
  1. A Record : Resolve the domain name into ipv4 address. Domain → ipv4.
  2. AAAA Record : resolve the domain name to ipv6 address.
  3. Cname Record : Another domain name. Helps to manage multiple subdomain.
  4. MX Record : Mail server hostname (+priority). Where to send mail of the domain.
  5. NS record : Authoritative DNS server hostname. Who manages this domain's DNS

- Run: dig google.com — identify the A record and TTL (Time to leave)  from the output.
  TTL = 164 Seconds
  ![TTL]()

## Task 2: IP Addressing

- What is an IPv4 address? How is it structured? (e.g., 192.168.1.10)
  IPV4 is identity of network device or host in network. 
Difference between public and private IPs — give one example of each
What are the private IP ranges?
10.x.x.x, 172.16.x.x – 172.31.x.x, 192.168.x.x
Run: ip addr show — identify which of your IPs are private
