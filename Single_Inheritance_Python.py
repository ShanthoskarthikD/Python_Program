class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

child_obj = Child()
child_obj.display() 
child_obj.show()     
