# -------Class defination-----
class Product:


    # ------Similar to constructor
    def __init__(self,prodId,prodName):
        self.prodId = prodId
        self.prodName = prodName
    
    def __str__(self):
        return "ID : " + str(self.prodId) + " Name : " + self.prodName
    
    def __gt__(self,obj1):
        return self.prodId > obj1.prodId


# -----------Obj creation-----

obj = Product(1010,"Note Book")
obj1 = Product(102,"Pen")
print(obj.prodId,obj.prodName)
print(obj1.prodId,obj1.prodName)
print(obj > obj1)

