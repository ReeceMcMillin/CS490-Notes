# Challenges

### Heterogeneity
As distributed systems scale, the ability of different systems to talk
to each other becomes a serious concern.
    - the internet allows users to access services and applications from an
extremely diverse set of devices and networks
    - data types may be represented differently on different sorts of
    hardware
    - different systems may provide different APIs to the same protocols
    - different programming languages use different representations for
    various data structures
    - differences must be addressed via [marshalling](../chapter-4/marshalling.md)
       if applications using these languages are to communicate with each other

{:.def term="Middleware"}
A software layer that provides a programming abstraction as
well as masking the heterogeneity of the underlying networks, hardware,
operating systems, and programming languages.

Most middleware is implemented over the Internet protocols, which
themselves mask the differences of the underlying network. *All*
middleware deals with the differences in operating systems and hardware.
More on this in [Chapter 4](../chapter-4/index.md).

*Mobile code* refers to program code that can be transferred between
computers and run at the destination, such as Java Applets (or anything
via log4j). The *virtual machine* approach provides a way of making code
executable on a variety of host computers: generate code for a
particular virtual machine instead of generating it for every possible
consumer.

### Openness
*Openness* refers to the characteristic that determines whether a system
can be extended and reimplemented in various ways. For distributed
systems, how well can a new resource-sharing service be added and made
available for use by clients? This **requires** that key interfaces be published, but this is only the
starting point.

Systems designed to support resource sharing in this way are termed *open distributed systems*
to emphasize the fact that they are extensible.
### Security
Security for information resources has 3 components:
    - confidentiality
    - integrity
    - availability
### Scalability
A system is *scalable* if it will remain effective when there is a
significant increase in the number of resources and/or users.

Challenges relating to scalability include:
    - controlling the cost of physical resources
        - a system with \\(n\\) users should require at most \\(O(n)\\)
        additional resources
    - controlling the performance loss
        - algorithms that use hierarchic structures scale better than
        those that use linear structures
        - performance should be no worse that \\(O(\log{n})\\)
    - preventing software resources running out
        - consider IPv4
    - avoiding performance bottlenecks
        - in general, algorithms should be decentralized
### Failure Handling
Failures in distributed systems are *partial*, meaning some components
can fail while others continue to function. Particular techniques for
dealing with failure might be:
    - detecting failure
        - not all failures can be detected, but some can!
    - masking failure
        - messages can be retransmitted, data can be written to multiple
        disks, etc
    - tolerating failure
    - recovery from failure
        - software designed to respond to failure with recovery actions
    - redundancy
        - no *single* point of failure - one goes down, the rest cover

The availability of a system is a measure of the proportion of time that
it is available for use.
### Concurrency
Several clients might attempt to access a resource at the same time, so
shared resources must be treated with care. Further reading in
Chapter 7 and [Chapter 17](../chapter-17/index.md).
### Transparency
*Transparency* is the concealment of the separation of components in a
distributed system from both the user and application programmer. This
has the goal of portraying the system as a *whole* rather than a
collection of independent components.
    - ***access transparency*** enables local and remote resources to be
    accessed using identical operations
    - ***location transparency*** enables resources to be accessed without
    knowledge of their physical or network location 
    - *concurrency transparency* enables several processes to operate
    concurrently using shared resources without interference between
    them
    - *replication transparency* enables multiple instances of resources
    to be used to increase reliability and performance without knowledge
    of the replicas by users or programmers
    - *failure transparency* enables concealment of faults, allowing
    users and programs to complete their tasks despite component failure
    - *mobility transparency* allows the movement of resources and
    clients within a system without affecting the operation of users or
    programs
    - *performance transparency* allows the system to be reconfigured to
    improve performance as loads vary
    - *scaling transparency* allows the system and applications to
    expand in scale without change to the system structure or the
    application algorithms

Access transparency and location transparency are the most important and
are sometimes referred to together as *network transparency*.
### Quality of Service
The main nonfunctional properties of systems that affect the quality of
the service experienced by clients and users are:
    - reliability
    - security
    - performance
    - adaptability (sometimes)
