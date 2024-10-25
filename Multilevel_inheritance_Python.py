class GrandParent:
    def display_grandparent(self):
        print("This is the GrandParent class")

class Parent(GrandParent):
    def display_parent(self):
        print("This is the Parent class")


class Child(Parent):
    def display_child(self):
        print("This is the Child class")

child_obj = Child()
child_obj.display_grandparent() 
child_obj.display_parent()       
child_obj.display_child()       
