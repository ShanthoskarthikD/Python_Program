class BaseClass:
    def display(self):
        print("BaseClass Display method")
class DerivedClass(BaseClass):
    def display(self):
        print("DerivedClass Overridden Display method")		
base_obj = BaseClass()
base_obj.display() 
derived_obj = DerivedClass()
derived_obj.display() 
base_obj_ref = derived_obj
base_obj_ref.display() 
