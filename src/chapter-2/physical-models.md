# Physical Models

{:.def}
A **physical model** is a representation of the underlying hardware
elements of a distributed system that abstracts away from specific
details of the computer and networking technologies involved.

Baseline model: an extensible set of computer nodes interconnected by a
network for the required passing of messages.

Three generations of distributed systems:
1. Early distributed systems:
    - 10-100 nodes on a LAN
    - openness not a primary concern
2. Internet-scale distributed systems
    - began to emerge in the 90s
    - physical model is an extensible set of nodes interconnected by a
    *network of networks*
    - led to increasing emphasis on open standards/middleware
3. Contemporary distributed systems
    - today's physical models include mobile nodes such as laptops and
    smartphones
    - ubiquitous computing has led to architectures where computers are
    embedded in the surrounding environment
    - cloud computing has led to a move from autonomous nodes to a pool
    of provider nodes for a given service

This evolution has resulted in a significant increase in heterogeneity
of devices and variation in networking technologies.
