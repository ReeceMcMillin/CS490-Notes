# Introduction

{:.def term="Distributed System"}
A system in which hardware or software components located at networked computers communicate and coordinate their actions *only* by passing messages.

This definition has several consequences:
    - concurrency
    - no global clock
    - independent failures

The prime motivation for constructing and using distributed systems
stems from a desire to *share resources*.
    - a *resource* can range from hardware components to software resources
