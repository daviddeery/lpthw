# Now it gets tricky...
# We open a file with open() method.
# We then read the file with read() method and print the contents.
# We close the file with close() method.

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {filename}:".format(filename=filename))
print(txt.read())

print("Type the filename again:")
file_again = input(" >")

text_again = open(file_again)

print(text_again.read())

txt.close()

text_again.close()
