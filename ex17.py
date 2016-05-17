# the exists method tests if a path exists - returns false for broken symbolic links or no path
# we are also opening and closing files. Reading and writing data.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {from_file} to {to_file}".format(from_file=from_file, to_file=to_file))

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is {length} bytes long".format(length=len(indata)))

print("Does the file exist? {exist}".format(exist=exists(to_file)))
print("Ready, hit RETURN to continue, CTR-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
