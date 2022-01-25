# IPC and Remote Invocation

{:.note}
Related Reading:
    - [Chapter 4 - Interprocess Communication](../chapter-4/index.md)
    - [Chapter 5 - Remote Invocation](../chapter-5/index.md)

## Interprocess Communication (IPC)

Underlying IPC primitives:
- sockets
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


