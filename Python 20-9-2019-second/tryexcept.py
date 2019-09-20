class MyError(Exception):
    pass
def validate(data):
    if data > 0:
        return True
    else:
        raise MyError

try:
    n1 = int(input("Enter no : "))
    n2 = int(input("Enter the no: "))
    if validate(n1) and validate(n2):

        n3 = n1/n2
        print("Result",n3)
except MyError:
    print("-ve values are not allowed")
except ValueError:
    print("Only digits are allowed")
finally:
    print("Executes everytime")
print("----------Done-------")