# In the case you want to override a function from the parent class, just define a function with the same name in the subclass.
class Parent(object):

    def override(self):
        print("PARENT override()")
        
class Child(Parent):

    def override(self):
        print("CHILD override()")
        
dad = Parent()
son = Child()

dad.override()
son.override()                
