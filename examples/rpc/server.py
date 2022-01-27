import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

data = {
    "John": {"name": "John", "age": 30},
    "Alice": {"name": "Alice", "age": 20},
}

def today():
    print("getting today's date...")
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def add(x, y):
    print(f"adding {x} and {y}...")
    return x + y

def get(name):
    print(f"getting info for {name}...")
    if name in data
    return data[name]

server = SimpleXMLRPCServer(("localhost", 8000))

print("listening on port 8000...")

server.register_function(today, "today")
server.register_function(add, "add")
server.register_function(data.get, "get")

server.serve_forever()