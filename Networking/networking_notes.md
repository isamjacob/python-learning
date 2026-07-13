The OSI model 

It's framework that explains how data travels from one computer to another. 

Analogy Sending a letter - 

You write a letter      - Application layer 
Put in envelop          - Presentation layer
Add address             - Session layer
Post office recieves it - Transport layer
Sorting facility        - Network layer
Delivery truck          - Data Link layer
Roads                   - Physical layer

Layer 7 → Application  → HTTP, FTP, DNS, SMTP
Layer 6 → Presentation → Encryption, Compression, SSL
Layer 5 → Session      → Managing connections
Layer 4 → Transport    → TCP, UDP, Ports
Layer 3 → Network      → IP addresses, Routing
Layer 2 → Data Link    → MAC addresses, Switches
Layer 1 → Physical     → Cables, WiFi signals

*Layer 7 Application Layer* 

What you directly interact with.
Protocols: HTTP, HTTPS, FTP, SMTP, DNS

Examples:
→ Browser requests webpage (HTTP)
→ Email client sends email (SMTP)
→ Typing a domain name (DNS)

*Layer 6 Presentation*

Translates, encrypts, compresses data.

Examples:
→ HTTPS encrypts your data (SSL/TLS)
→ Images compressed before sending
→ Data converted to readable format

*Layer 5 Session*

Manages connections between applications.
Opens, maintains, closes sessions.

Examples:
→ Login session on a website
→ Video call connection
→ API connection maintained

*Layer 4 Transport*

Responsible for end-to-end delivery.
Two protocols: TCP and UDP

TCP → reliable, ordered delivery
UDP → fast, no guarantee

Examples:
→ Downloading a file (TCP)
→ Video streaming (UDP)
→ Online gaming (UDP)

*Layer 3 Network*

Handles routing between networks.
Protocol: IP (Internet Protocol)

Examples:
→ Your IP address: 192.168.1.1
→ Router decides path for your data
→ Data travels across internet

*Layer 2 Data Link*

Transfers data between devices on same network.
Uses MAC addresses.

Examples:
→ Your laptop connects to WiFi router
→ Switch sends data to correct device
→ MAC address: 00:1A:2B:3C:4D:5E

*Layer 1 Physical*

Actual physical transmission.
Cables, radio waves, fiber optics.

Examples:
→ Ethernet cable
→ WiFi radio signals
→ Fiber optic light pulses

*TCP/IP Model*

Application  → HTTP, FTP, DNS, SMTP  (OSI layers 5,6,7)
Transport    → TCP, UDP              (OSI layer 4)
Internet     → IP, ICMP              (OSI layer 3)
Network      → Ethernet, WiFi        (OSI layers 1,2)

*TCP vs UDP*

TCP                          UDP

Reliable delivery            No guarantee
Ordered packets              No order
Error checking               No error checking
Slower                       Faster
Connection based             Connectionless

Use for:                     Use for:
→ File download              → Video streaming
→ Web browsing               → Online gaming
→ Email                      → DNS queries
→ Database queries           → Live broadcasts

*TCP 3-Way Handshake*

First the client send a SYN request 
then the server acknowledge it and sent a ACK 
clint also sends ACK and connection is established 

SYN = Syncronise 
ACK = Acknowledge

*IP ADDRESS*

IPv4 -> 192.168.1.1
IPv6 -> 2001:0db8:85a3:0000:0000:8a2e:0370:7334

*Private IP ranges*

10.0.0.0 -> 10.255.255.255
172.16.0.0 -> 172.31.255.255
192.168.0.0 -> 192.168.255.255

*Special IP*

127.0.0.1       -> localhost 
0.0.0.0         -> All interfaces
255.255.255.255 -> broadcast

*DNS - Domain Name System*

You type: google.com
DNS resolves: 142.250.80.46
Browser connects to: 142.250.80.46

*DNS resolution process*

1. Browser checks local cache
2. Asks local DNS resolver (your router)
3. Asks Root DNS server
4. Asks TLD server (.com, .org)
5. Asks Authoritative DNS server
6. Gets IP address → connects!

*HTTP and HTTPS*

HTTP = Hyper Text Transfer Protocol

Request:
GET /students HTTP/1.1
Host: api.example.com
Authorization: Bearer token123

Response:
HTTP/1.1 200 OK
Content-Type: application/json
[{"id": 1, "name": "Sam"}]

*HTTP Methods*

GET    → retrieve data
POST   → send/create data
PUT    → update data
DELETE → delete data
PATCH  → partial update

*HTTP Status Codes*

2xx → Success
  200 OK
  201 Created
  204 No Content

3xx → Redirection
  301 Moved Permanently
  302 Found

4xx → Client Error
  400 Bad Request
  401 Unauthorized
  403 Forbidden
  404 Not Found
  429 Too Many Requests

5xx → Server Error
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable

*HTTPS = HTTP + SSL/TLS encryption*

HTTP  → data sent as plain text (anyone can read!)
HTTPS → data encrypted (safe!)

*PORTS*

Port = specific door on a computer for specific service

Port 80   → HTTP
Port 443  → HTTPS
Port 22   → SSH
Port 21   → FTP
Port 25   → SMTP (email)
Port 3306 → MySQL
Port 5432 → PostgreSQL
Port 6379 → Redis
Port 8000 → FastAPI (default)
Port 3000 → Node.js (default)

*Full address = IP + Por*

192.168.1.1:8000
              
   IP addr :  Port

