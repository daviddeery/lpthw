# if you put functions in a base class (i.e., Parent) then all subclasses (i.e., Child) will automatically get those features

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    pass
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit()            
