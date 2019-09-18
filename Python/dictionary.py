
# ---------Dict---------
d1 = {}
d2 = dict()

# Key unique and value can be anything 

d1 = {1:"John", 2:"Bob", 3:"Alex"}
# print(d1.get(2))
# print(d1[1])
print(d1.keys())
for val in d1.keys():
    print(d1.get(val),'________',d1[val])

print(d1.values())
for v in d1.values():
    print(v)

print(d1.items())

for k,v in d1.items():
    print(k,v)

d1[1] = "Jim"
d1[55]= "Rajesh"
d1["one"]= "Jerry"
print(d1)
