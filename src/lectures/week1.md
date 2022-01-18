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

