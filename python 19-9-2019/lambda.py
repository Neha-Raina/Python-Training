# lambda arg-list : return value

# x = lambda a,b : a+b
# print(x(10,20))

# def myfilter(mylist,criteria):
#     new_list= []
#     for item in mylist:
#         if criteria(item):
#             new_list.append(item)
#     return new_list

# print(myfilter([11,2,4,5,77],lambda e :e>1))
# print(myfilter([11,2,4,5,77],lambda e : e%2==0))

def myfilter(mylist,criteria):
    new_list= []
    for item in mylist:
        x = criteria(item)
        new_list.append(x)
    return new_list

print(myfilter([11,2,4,5,77],lambda e : e**2))
print(myfilter([11,2,4,5,77],lambda e : e+10))
