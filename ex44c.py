# Introducing the Python built in method - super() - the super() method is aware of inheritence and will get the parent class.
class Parent(object):

    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.altered()
son.altered()                
