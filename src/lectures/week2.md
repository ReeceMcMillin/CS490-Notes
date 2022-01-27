# IPC and Remote Invocation

{:.note}
Related Reading:
    - [Chapter 4 - Interprocess Communication](../chapter-4/index.md)
    - [Chapter 5 - Remote Invocation](../chapter-5/index.md)

## Interprocess Communication (IPC)

Underlying IPC primitives:
- sockets [^1]
- message passing
- multicast support
- overlay network

### Characteristics
- two primitive messaging operations
    - send: one process sends
    - receive: another process receives
- synchrony:
    - synchronous (blocking)
        - sender waits until message is sent
        - receiver waits for messages
    - asynchronous (non-blocking)
        - sender sends message to the queue and proceeds immediately
        - receiver is notified whenever there's a new message
- message destination
    - naming of nodes
    - typically a tuple: (ip address, port)
- reliability
    - is delivery guaranteed?
- ordering
    - various orders are possible!
    - fifo is common (sender order)

### Sockets for IPC
- most widely used IPC mechanism
    - usually used in client-server architecture
    - server process creates a socket and "binds"
    - client process connects to the server socket in the specified port
    - once connected, they send/receive messages

UDP - Echo Server (Java)

### Serialization/Marshalling

{:.def term="Serialization"}
The process of converting structured data into a byte sequence

{:.def term="Marshalling"}
The process of taking a collection of data items and assembling them
into a form suitable for transmission in a message

### Remote Invocation

{:.aside}
It's impossible for a client to tell whether or not a server has failed!

Three dominant paradigms:
- request-reply
    - pattern on top of message passing which supports two-way exchange
    of messages
    - usually encountered in client-server architecture
    - relatively low-level
    - protocol should handle failures
- remote procedure call
    - client programs call "procedures" (functions) transparently in
    server program
    - usually, client and server run on different computers/machines
- remote method invocation (RMI)
    - RPC on objects
    - one object in one process calls methods of another object in
    another process

#### Request-Reply Protocols

Failures
- implementations:
    - usually UDP, but TCP is also possible
    - can suffer from omission failures
- order is not guaranteed
- message identifiers:
- every request gets a unique ID
- usually 32-bit
- request (or reply) is lost
    - client waits for result to come and result never appears
    - client times out and resends duplicate request
- server may receive "duplicate" requests
    - server can detect and discard duplicate requests
    - server stores result and returns
    - server executes the same operation twice
        - good for "idempotent" operations [^2]

#### HTTP
- example of RR protocol
    - client requests "web pages" from a *web server*

HTTP is implemented on TCP (server port 80)
- client requests, server accepts connection
- client sends request message to server
- server sends reply message to client
- connection is closed

#### REST

{:.aside}
REST is a set of architectural constraints, **not a protocol or standard**.

- modern day remote invocation method via HTTP
- REST:
    - **RE**presentational
    - **S**tate
    - **T**ransfer
- key issues:
    - client transfers a "representation" of the state of the resource
    to the server
        - not just GET, PUT but mor einfo in request body
        - usually in JSON
    - server processes request and returns results
- REST can be thought of as similar to HTTP but for web pages

### Remote Procedure Call (RPC)
RPC is a major breakthrough in distributed computing! [^3]
- allows one program (client) to call a function in another program (server)
- SUN used this in their Networked File Systems (NFS)
- Designed in client-server architecture

- Service interface abstracts the communication
    - client only knows *what* a function does, not *how*
    - server implements procedure and executes
    - interfaces are usually defined using IDL (Interface Definition
    Language)

#### RPC Call Semantics

RPC can be implemented via request-reply protocols
- needs stronger guarantees

Local function calls are *exactly-once*, but RPC semantics can vary

| retransmit request message | duplicate filtering | re-execute procedure or retransmit reply | call semantics|
|-|-|-|-|
|no|n/a|n/a|maybe|
|yes|no|re-execute procedure|at-least-once|
|yes|no|re-execute|at-least-once|
|yes|yes|retransmit|at-most-once|

#### RPC Implementation
Client
- for each procedure in service, there's a **stub** procedure (aka
  *proxy*)
- stub procedure behaves like it's running locally
    - actually marshals the procedure ID and arguments to the server
    - this happens via communication module

Server
- the reverse operation (stub - call)
- dispatcher
    - selects appropriate stub to call based on procedure ID

Popular implementations:
- JSON-RPC
- gRPC (Google RPC)
    - RPC using protocol buffers [^4]

#### Remote Method Invocation

RPC on objects within OOP
- mainly in Java

Two main concepts:
- remote object references
- remote interfaces

Popular implementations:
- Java RMI (industry leader for a while back in the 90s)
- CORBA (Common Object Request Broker Architecture)

### RPC Example in Python
```python
# server.py
import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def add(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))

print("listening on port 8000")

server.register_function(today, "today")
server.register_function(add, "add")

server.serve_forever()
```

```python
# client.py
import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")

added = proxy.add(1, 2)

print(f"Today: {converted.strftime('%d.%m.%Y, %H:%M')}")
print(f"Added: {added}")
```


# Further Reading

[^1]: Various socket programming resources:
      [beej's guide (C)](https://beej.us/guide/bgnet/html/index-wide.html) - 
      [ibm sample socket programs (C)](https://www.ibm.com/docs/en/zos/2.1.0?topic=interface-sample-c-socket-programs) - 
      [visuals-heavy ppt](https://www.csd.uoc.gr/~hy556/material/tutorials/cs556-3rd-tutorial.pdf) - 
      [code-heavy tutorial](https://www.binarytides.com/socket-programming-c-linux-tutorial/)


[^2]: [AWS - Making Retries Safe with Idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

[^3]: [Dave Marshall - Remote Procedure Calls (in C)](https://users.cs.cf.ac.uk/Dave.Marshall/C/node33.html)

[^4]: [gRPC homepage with language-specific tutorials](https://grpc.io/)
