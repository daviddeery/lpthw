print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \
t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------")
print(poem)
print("-----------------")


five = 10 - 2 + 3 - 6
print("This should be five: {five}".format(five=five))
 
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {sp}".format(sp=start_point))
print("We'd have {b} beans, {j} jars and {c} crates.".format(b=beans, j=jars, c=crates))

start_point = start_point / 10

print("We can also do that this way:")
t = secret_formula(start_point)
print("We'd have {b} beans, {j} jars and {c} crates.".format(b=t[0], j=t[1], c=t[2]))      
