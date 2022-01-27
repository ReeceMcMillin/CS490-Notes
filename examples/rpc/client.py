import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")

added = proxy.add(1, 2)

alice = proxy.get("Alice")
# reece = proxy.get("Reece")

print(f"Today: {converted.strftime('%d.%m.%Y, %H:%M')}")
print(f"Added: {added}")
print(f"Alice's age: {alice.get('age')}")
# print(f"Reece's age: {reece.get('age')}")