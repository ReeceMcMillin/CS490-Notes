# Trends in Distributed Systems

## The Internet
Enough said, right?

## Mobile & Ubiquitous Computing
Increasingly, companies use techniques such as *location-aware* or
*context-aware* computing to provide users with highly targeted content.
This level of mobility also introduces new challenges for distributed
systems, such as:
    - variable connectivity
    - outright disconnection
    - maintain operation in the face of mobility

{:.def term="Ubiquitous Computing"}
The harnessing of many small, cheap computational
devices that are present in users' physical environments, including
home, office, and natural settings.

The suggestion with ubiquitous computing is that, eventually, computing
devices will be so pervasive that they're scarcely noticed. Their
computational behavior will be transparently and intimately tied with
their physical function. Although there is some overlap, ubiquitous and
mobile computing are separate.

A primary goal of ubiquitous computing is *spontaneous interoperation*,
whereby associations between devices are routinely created and
destroyed. The challenge is to make this interoperation fast and
convenient, even though the user may be visiting the area for the first
time. The process of enabling a visitor's device to communicate on the
host network and associate with local services is called *service
discovery*.

## Distributed Multimedia Systems
The crucial characteristic of continuous media types is that they
include a *temporal* dimension. For example, there may be restrictions
on minimum acceptable FPS throughput or real-time latency.

Distributed multimedia systems are largely concerned with:
    - providing support for an extensible range of formats
    - providing a range of mechanisms to ensure a desired quality
    - providing resource management strategies
    - providing adaptation strategies to deal with loss of
    quality/service

## Distributed Computing as a Utility
Many companies have an interest in promoting distributed resources as a
commodity or utility in the style of water or electricity. This opens
the door for a *rent-based* service model rather than an ownership-based
model.
    - SaaS, IaaS, *aaS

{:.def term="Cloud"}
A set of internet-based application, storage, and computing
services sufficient to support most users' needs, thus enabling them to
largely or totally dispense with local data storage and application
software.

Clouds are generally implemented on *cluster computers*, sets of
interconnected computers that cooperate closely to provide a single,
integrated high-performance computing capability.
