# Good job!! Used argv to pass arguments via the command line and contained things into a function.
# Excellent - now you've incorporated a way to handle the exception in case inc is not specified. 
# How can you make it just handle only one argument??
from sys import argv

script, limit, inc = argv
limit = int(limit)
inc = int(inc)

def counter(limit, inc):

    i = 0
    numbers = []
    
    try:
        inc
    except NameError:
        inc = 1

    while i < limit:
        print("At the top i is {i}".format(i=i))
        numbers.append(i)
    
        i = i + inc
        print("Numbers now: {numbers}".format(numbers=numbers))
        print("At the bottom i is {i}".format(i=i))
    
    
    print("The numbers: ")

    for num in numbers:
        print(num)    
        
counter(limit, inc)        
