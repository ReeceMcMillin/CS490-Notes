# Characterization of Distributed Systems

{:.note}
Related reading:
    - [Chapter 1 - Characterization of Distributed Systems](../chapter-1/index.md)
    - [Chapter 2 - System Models](../chapter-2/index.md)

## Administrative
- in-person: tuesday/thursday 11:30-12:45 in Haag 201
- office hours (monday 3-4pm): [zoom link](https://umsystem.zoom.us/j/94171457064?pwd=N2plOVd5eGZFWFk1Z1plNFJ3OG9EUT09)
- exams: open-book
- preferred communication: canvas
- preferred language for homework: python or go
    - learning go:
        - [learn go with tests](https://quii.gitbook.io/learn-go-with-tests/)


### Activities

| activities | weights |
| - | - |
| homework (4) | 40% |
| programming (2) | 20% |
| midterm exam | 20% |
| final exam | 20% |

- midterm exam and final exam are mutually exclusive, final not
  comprehensive

## What is a Distributed System?

- distributed!
    - message passing
    - no single point of failure
- system!
    - more than one entity
    - working in tandem

definition
- collection of automata whose distribution is transparent to the user
  so the system appears as one machine
- usually use some kind of "client-server" organization

{:.def term="Distributed System (Tanenbaum)"}
A collection of independent computers that appear to the users of the
system as a single computer.
<!--{:def term="term"}
possibly multi-line definition
{/def}-->

{:.def term="Distributed System (textbook)"}
A system in which hardware or software components located at networked
computers communicate and coordinate their actions only by passing
messages.

A **message** has some sort of *semantic meaning* - more than just bits and bytes

A communication network itself is not a distributed system unless
certain "applications" are running on it
- applications are the primary clients of a distributed system
- it's not the *network* that matters, it's the *application* that matters
    - ("matters" when defining a distributed system)

{:.def term="Distributed System (class)"}
A collection of *entities*, each of which is *autonomous, programmable,
and failure-prone*, and which communicate through an *unreliable*
communication medium.

- Entity: a "process" on a device
- Communication media: wired or wireless

Three main aspects:
- distributed algorithms
    - group communication, consensus, time synchronization
- distributed services
    - remote invocation, replication, security
- distributed systems
    - distributed hash tables
    - p2p systems
    - cloud computing

Attributes of distributed systems:
- concurrency
- no global clocks
- independent failures
    - distributed systems can be characterized by the *independence* of
the participating nodes

{:.def term="Cloud Computing"}
The term applied to distributed computing infrastructure packaged as a
utility - computing resources are *rented* rather than owned by
end-users.

The cloud computing model can be applied to physical resources as well
as logical resources.

Challenges in Distributed Systems
- heterogeneity
- openness
    - can be extended and reimplemented in various ways
- security
- scalability
- failure handling
- transparency
    - system perceived as a whole rather than a collection of
    independent components

## System Models
- [ Physical Models ](../chapter-2/physical-models.md)
    - hardware composition of a system of computers and their
  interconnection networks
- [ Architectural Models ](../chapter-2/architectural-models.md)
    - in terms of computational and communicational elements
- [ Fundamental Models ](../chapter-2/fundamental-models.md)
    - abstract model to examine aspects of a system

### Physical Models
- baseline physical model
    - a set of computers connected by a network
### Architectural Models
- "computers" are replaced with "entities"
    - abstract transformation
- communication entities
    - processes: executing programs
    - processes communicate
        - ([inter-process communication](../chapter-4/index.md))
    - from programming perspective, more abstractions are possible
        - objects (OOP style)
        - components
            - objects and related dependencies
        - web services
            - combines objects and components as a "service"
            - exposes APIs for other process/applications to call
- communication paradigms
    - direct communication
        - Interprocess Communication (IPC)
            - low-level
        - Remote Invocation (RI)
            - two-way exchange of messages between entities
            - several methods
                - request-reply protocols
                - remote procedure call (RPC)
                    - one process calls procedure/function in another
                    process
                - remote method invocation (RMI)
                    - RPC in the context of distributed objects
            - sender sends to receiver
            - both know each other and exist at the same time
            - "coupled" in space and time
    - indirect communication
        - uncoupled
            - senders don't know who they're sending to
                - space uncoupled
            - senders and receivers do **not** exist at the same time
                - time uncoupled
        - key techniques
            - group communication
            - pubsub
            - message queues
            - tuple spaces
            - distributed shared memory
- roles and responsibilities
    - most popular model: client-server architecture
        - roles:
            - clients "request"
            - servers "reply" or "respond"
    - peer-to-peer architecture
        - no single node acts as server
        - all nodes act as clients and servers
            - all are "peers"
        - examples: bittorrent, blockchain
- architectural patterns
    - layering (popular)
        - vertical "stack" of services where lower-level services
        provide abstract interfaces for higher-level services to call
### Fundamental Models
- three questions:
    - what are the main **entities** in the system?
    - how do they **interact**?
    - what are the characteristic that affect their **individual** and
    **collective** behavior?
- sender sends "messages" to a receiver through a "channel"
    - two basic/primitive operations:
        - send
        - receive
- properties of the communication channel:
    - latency
    - bandwidth
    - jitter

{:.def term="Distributed Algorithm"}
A sequence of steps, including sending and receiving of messages and
update internal state within each process.

- two variants based on **bound on timing of events**
- synchronous systems
    - take bounded (lower and/or upper) time for
        - executing each step of a process
        - receiving a message after the message has been transmitted
        - bounded clock drift
- asynchronous systems
    - have *no known bound* on how much time it can take on an operation

#### Ordering of Events

The order in which messages are received cannot take the order those
messages are sent into account
- asynchronous nature of distributed systems

#### Failure Model

| class of failure | affects | description |
|*---*|*---*|*---*|
|fail-stop | process|
| crash|process |
|omission |channel |
| send-omission|process |
|receive-omission |process |
| arbitrary (byzantine)|process or channel |

timing failures:
- clock
    - affects process
    - process's local clock exceeds bounds on rate of drift from real
    time
- performance
    - process
        - process exceeds bounds on interval between two steps
    - channel
        - a message's transmission takes longer than the stated bound

# Major Questions in this Course

What are the entities and how do they communicate?
What sorts of failures are we assuming?
- fail-stop
- omission
- arbitrary (byzantine)
