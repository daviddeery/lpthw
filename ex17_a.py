from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {from_file} to {to_file}".format(from_file=from_file, to_file=to_file))
import pdb;pdb.set_trace()
indata = open(from_file).read()

print("The input file is {length} bytes long".format(length=len(indata)))

print("Does the file exist? {exist}".format(exist=exists(to_file)))
print("Ready, hit RETURN to continue, CTR-C to abort.")
input()

out_file = open(to_file, 'w').write(indata)

print("Alright, all done.")

to_file.close()
from_file.close()
