class ComplexNo:

    def __init__(self,real = 0,img = 0):
        self.real = real
        self.img = img

    def __add__(self,other): 
        x = self.real +other.real
        y = self.img + other.img
        result = str(x) +   " + j" + str(y)
        return result

    def __str__(self):
        return str(self.real) + " + j" + str(self.img)

obj1 = ComplexNo(10,5)
obj2 = ComplexNo(7,2)
print(obj1 + obj2)

