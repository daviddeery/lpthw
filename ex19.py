# functions can accept numbers directly or variables, it's possible to do math inside as well as math plus variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {cheese_count} cheeses!".format(cheese_count=cheese_count))
    print("You have {boxes_of_crackers} boxes of crackers".format(boxes_of_crackers=boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

    
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)    
