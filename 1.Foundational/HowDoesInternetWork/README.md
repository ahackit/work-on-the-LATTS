# LATT-HowDoesInternetWork
Learn All The Things - How does the internet work?

For further reading: http://www.theshulers.com/whitepapers/internet_whitepaper/index.html


## Internet Addresses

- Internet is a network of computers. Each computer connected must have a unique address.
- You typically given a temporary public IP when you connect to the interwebs through your ISP.
- Your local IP is usually given from your router or a DHCP server.

## Communication using packets and Protocol Stacks

- Now you have IP address to communicate you will send Packets
- Protocal stack is responsible for delivering those packets. Every computer usually has this built into the OS
  - TCI/IP Protocol
  - Applications Protocols Layer: Protocols specific to applications such as WWW, e-mail, FTP, etc.
  - Transmission Control Protocol Layer: TCP directs packets to a specific application on a computer using a port number.
  - Internet Protocol Layer: IP directs packets to a specific computer using an IP address.
  - Hardware Layer: Converts binary packet data to network signals and back.

## Routing

- Routers are packet switches.
- Each router knows its sub-networks and IP addresses they use.
-  If the network containing the IP address is found, the packet is sent to that network. If the network containing the IP address is not found, then the router sends the packet on a default route, usually up the backbone hierarchy to the next router. Hopefully the next router will know where to send the packet.

## Domain Names/Address Resolution

- DNS is a distributed database which keeps track of computer's names and their corresponding IP addresses on the Internet.
- If a DNS server doesn't have your address, it will send it to another DNS server to find it.

## Application Protocols 
### HTTP and the World Wide Web
- HTTP is the protocol that web browsers and web servers use to communicate with each other over the Internet.
- HTTP is a connectionless text based protocol. Clients (web browsers) send requests to web servers for web elements such as web pages and images. After the request is serviced by a server, the connection between client and server across the Internet is disconnected.
- When you type a URL into a web browser, this is what happens:
  - If the URL contains a domain name, the browser first connects to a domain name server and retrieves the corresponding IP address for the web server.
  - The web browser connects to the web server and sends an HTTP request (via the protocol stack) for the desired web page.
  - The web server receives the request and checks for the desired page. If the page exists, the web server sends it. If the server cannot find the requested page, it will send an HTTP 404 error message. (404 means 'Page Not Found' as anyone who has surfed the web probably knows.)
  - The web browser receives the page back and the connection is closed.
  - The browser then parses through the page and looks for other page elements it needs to complete the web page. These usually include images, applets, etc.
  - For each element needed, the browser makes additional connections and HTTP requests to the server for each element.
  - When the browser has finished loading all images, applets, etc. the page will be completely loaded in the browser window.

### SMTP and Electronic Mail
-  E-mail uses an application level protocol called Simple Mail Transfer Protocol or SMTP
- SMTP is also a text based protocol, but unlike HTTP, SMTP is connection oriented
- When you open your mail client to read your e-mail, this is what typically happens:

  - The mail client (Netscape Mail, Lotus Notes, Microsoft Outlook, etc.) opens a connection to it's default mail server. The mail server's IP address or domain name is typically setup when the mail client is installed.
  - The mail server will always transmit the first message to identify itself.
  - The client will send an SMTP HELO command to which the server will respond with a 250 OK message.
  - Depending on whether the client is checking mail, sending mail, etc. the appropriate SMTP commands will be sent to the server, which will respond accordingly.
  - This request/response transaction will continue until the client sends an SMTP QUIT command. The server will then say goodbye and the connection will be closed.

## Transmission Control Protocol
  
- TCP is responsible for routing application protocols to the correct application on the destination computer.
- TCP is a connection-oriented, reliable, byte stream service.
- Connection-oriented means that two applications using TCP must first establish a connection before exchanging data. TCP is reliable because for each packet received, an acknowledgement is sent to the sender to confirm the delivery.