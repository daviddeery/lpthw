def counter(limit):

    i = 0
    numbers = []

    while i < limit:
        print("At the top i is {i}".format(i=i))
        numbers.append(i)
    
        i = i + 1
        print("Numbers now: {numbers}".format(numbers=numbers))
        print("At the bottom i is {i}".format(i=i))
    
    
    print("The numbers: ")

    for num in numbers:
        print(num)    
        
counter(10)        