# this one is like your scripts with argv
# def is the python way of making a function. All the variables inside a function, stay inside a function - unless the function returns them.
# a function with *args tells python to take all the arguments to the function and then put them in args as a list.
# In print_two(), only two variables can be passed - i.e. print_two("one", "two", "three") won't work.
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {arg1}, arg2: {arg2}".format(arg1=arg1, arg2=arg2))
    
# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: {arg1}, arg2: {arg2}".format(arg1=arg1, arg2=arg2))
    
# this just takes one argument
def print_one(arg1):
    print("arg1: {arg1}".format(arg1=arg1))

# this one takes no arguments
def print_none():
    print("I got nothin'.")
    
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()        
