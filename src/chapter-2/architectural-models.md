# Architectural Models

The architecture of a system refers to its separate components and the
relationships between them.

Major concerns: make the system
    - reliable
    - manageable
    - adaptable
    - cost-effective

Understanding the trade-offs inherent to choices similar to those identified in this
section is arguably the key skill in distributed systems design.

## Architectural Elements

Key questions:
- What are the entities that are communicating in the distributed
system?
- How do they communicate? More specifically, what *communication
paradigm* is used?
- What roles and responsibilities do they have in the overall
architecture?
    - Will they change?
- How are they mapped onto the physical distributed infrastructure?
    - In other words, what is their *placement*?

### Communicating Entities

The first two questions above are **essential** to an understanding of
distributed systems. From a system perspective, the entities that
communicate in a distributed systems are typically *processes*. This
leads to the view of a distributed system as processes coupled with
interprocess communication paradigms.

From a systems level, this is fine! From a programming perspective, other
abstractions have been proposed.
- objects
    - objects represent natural units of decomposition for some given
    problem domain
    - accessed via interfaces
    - interface definition language (IDL) provides a specification of
    methods on an object
    - a number of problems!
- components
    - components specify not only interfaces, but also the *assumptions*
    they make in terms of other components.
        - all dependencies are explicit
        - contract is more complete
        - this approach promotes higher *compositionality*
- web services
    - closely related to objects and components
        - approach based on encapsulation and access through interfaces
        - represent and discover services through web standards
    - expanded on in [chapter 9](../chapter-9/index.md)

### Communication Paradigms

Three types:
- *Interprocess communication* refers to the low-level support for
  communication between processes in distributed systems, including
    - message-passing primitives
    - direct access to the API offered by Internet protocols (socket
    programming)
    - support for multicast communication
    - expanded on in [chapter 4](../chapter-4/index.md)
- *Remote invocation* covers a range of techniques based on a two-way
  exchange between entities in a distributed system
    - results in the calling of a remote operation, procedure, or method
    - expanded on in [chapter 5](../chapter-5/index.md)
- *Request-reply protocols* are a pattern imposed on an underlying
  message-passing service to support client-server computing.
    - primitive, typically only used in embedded systems
    - this is the approach used by HTTP
    - most DSs will use remote procedure calls or remote method
    invocation
- *Remote procedure calls* allow procedures in processes on remote
  computers to be called as if they were processes in the local address
  space.
    - **access and location transparency**
- *Remote method invocation* strongly resembles remote procedure calls,
  but for distributed objects.
    - calling object can invoke a method in a remote object
    - underlying details are hidden from the user

{:.note}
All of these techniques have one thing in common:
communication represents a two-way relationship between a sender and a receiver, with
senders explicitly direction methods/invocations to the remote
receivers.

Receivers are typically aware of the identity of senders and both
typically exist at the same time. There are also indirect methods of
communication through a third entity allowing for higher decoupling:
- *space uncoupling*: senders don't need to know who they're sending to
- *time uncoupling*: senders and receivers do not need to exist at the
  same time

Key techniques for indirect communication include:
- *Group communication*: delivery of messages to a *set* of recipients
    - relies on the abstraction of a group represented by a group
    identifier
- *Publish-subscribe systems*: a large number of producers distribute
  information items of interest to a similarly large number of consumers
- *Message queues*: offer a point-to-point service where producer
  processes send messages to a specific queue, acting as the indirection between
  producers and consumers
- *Tuple spaces*: processes can place arbitrary items of structured data (tuples)
  in a space that can be read or removed by other processes
- *Distributed shared memory*: provide an abstraction for sharing data
  between process that don't share physical memory
    - programmers gain the abstraction of reading or writing shared data
    structures as if they were in their local address space
    - **distribution transparency**
    - expanded on in [chapter 6](../chapter-6/index.md)
### Roles and Responsibilities

Each process in a distributed system takes on certain roles which
establish the architectural model.

- *Client-server*: most often cited when distributed systems are
  discussed
    - scales poorly
- *Peer-to-peer*: no distinction between client and server
    - scales naturally with number of users
    - applications are composed of large numbers of peer processes
    running on separate computers
    - individual computers only hold a small responsibility for service

### Placement

Placement of a given client/server has few universal guidelines and needs to take into account
- patterns of communication between entities
- reliability of given machines and current load
- quality of communication between different machines
- etc.

To map services to multiple users, a service may be implemented as
several server processes in separate hosts. The servers may partition
the set of objects on which the service is based and distribute those
objects between themselves or replicate copies of them on several hosts.
- An example of this architecture is the *cluster*.

{:.def term="Cache"}
A store of recently used data objects that is closer to
one client or a particular set of clients than the objects themselves.

If a client needs an object, the caching service can check a local cache
first to save retransmitting potentially large payloads.

Some applications employ *mobile code*, which relies on a client to
download additional code to be run locally. The most common example of
this is the web, for example old-school Java applets (this book's
favorite example).

{:.aside note="i'm skeptical"}
is this really true? hard 2 say really idk i'm just adding text to test
justifying at this point lol

Extending that example are *mobile agents*, running programs that travel
from one computer to another in a network carrying out a task on
someone's behalf and returning with the results.
    - applicability may be limited


## Architectural Patterns

{:.aside note="lil summary deal"}
hi

testing

