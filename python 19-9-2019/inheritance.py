class Parent:
    def __init__(self,parent_property):
        self.parent_property = parent_property


# ---------------------------------------------------

class Child(Parent):
    def __init__(self,for_parent,child_property):
        super().__init__(for_parent)
        self.child_property = child_property

obj = Child(100,200)
print(obj.parent_property,obj.child_property)

# ----------------------------------------------------