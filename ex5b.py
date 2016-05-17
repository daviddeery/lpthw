name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # pounds
weight_kg = weight / 2.2 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches or %d cm tall." % (height, height_cm))
print("He's %d pounds or %d kg heavy." % (weight, weight_kg))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# This line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))
