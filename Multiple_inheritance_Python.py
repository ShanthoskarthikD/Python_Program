class ClassA:
    def display_A(self):
        print("This is ClassA")
class ClassB:
    def display_B(self):
        print("This is ClassB")
class ClassC(ClassA, ClassB):
    def display_C(self):
        print("This is ClassC")
obj = ClassC()
obj.display_A()  
obj.display_B()  
obj.display_C()  
