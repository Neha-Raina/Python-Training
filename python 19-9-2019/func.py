def add(x,y):
    return x+y
add(10,30)
print('Hello')

#  Input is converted into tuple

# def add_all(*args):
#     print(args)
# print(add_all(1,2,3,4,5,6))

# def add_all(*args):
#     total = 0
#     for val in args:
#         total+=val
#     return total
# print(add_all(1,2,3,4,5,6))

# def vol(l,w=1,h=1):
#     return l*w*h
# print(vol(5,4,3))
# print(vol(5,4))
# print(vol(5))

# # named list of parameters.

# def named_params(a = 8,**args):
#     print(a)
#     print(args)

# named_params(x=1,y=2,z=3)

if __name__ == "__main__":
    print(add(10,20))
    print(add(30,40))