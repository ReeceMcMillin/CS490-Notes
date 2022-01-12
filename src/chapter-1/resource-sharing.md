# Focus on Resource Sharing

Patterns of resource sharing vary widely in their scope and how closely
users are tied together.
    - search engine users never need to know about one another
    - cooperative workers in a particular organization may share *every*
    document together

{:.def}
Service: a distinct part of a computer system that manages a collection
of related resources and presents their functionality to users and
applications.

Resources in a distributed system are managed by a program that offers a
communication interface enabling the resource to be accessed and updated
reliably and constantly.

{:.def}
Server: a running program (a *process*) on a networked computer that
accepts requests from programs running on other computers to perform a
service and responds appropriately.

The requesting processes are referred to as *clients*, and the overall
approach is known as *client-server computing*.
