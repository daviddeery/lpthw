# input() method where the string is shown to the user - a prompt string - and the input is assigned to the variable on the left of the =

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print("So, you're {age} old, {height} tall and {weight} heavy.".format(age=age, height=height, weight=weight)) 
