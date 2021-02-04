# dictionary and its function
dict0={}
print(type(dict0))

d3={"Ritu":11,"Ravi":10,"Suraj":12,"prity":{"english":100,"science":80}}
# print(d3)
print(type(d3))
print(d3["Ritu"])

print(d3["prity"])
print(d3["Suraj"])

d3["harry"]="python"
# print(d3)

d2=d3.copy()
# print(d2)
del d3
# print(d3)
# print(d2)

# print(d2.get("harry"))
d2.update({"Soni": "5"})
# print(d2)
# print(d2.keys())
print(d2.items())
