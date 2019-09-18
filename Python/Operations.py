# List
ls = []
print(type(ls))
ls1 = list()
print(type(ls1))
ls.append(100)
ls.append(200)
print(ls)

#  Insert : you need to specify the location where you want to insert item

ls.insert(-1,111)

print(ls[-1])
#  negative index


list1 = [11,22,33,44,55]
# Slicing
ls1 = list1[2:5]
ls2 = list1[2:]
ls3 = list1[:2]
ls4 = ls1 * ls2
print(ls1)
print(ls2)
print(ls3)
print(ls4)
print(" Hi " + "3")


# Control statement