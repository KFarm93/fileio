#Imports argv
from sys import argv

#declares argv variables
script, filename = argv

#defines txt as "read mode"
txt = open(filename)

#prints text with argv variable filename added
print "Here's your file %r:" % filename
#reads and prints txt
print txt.read()
txt.close()

#prints another line
print "Type the filename again:"
#defines new variable "file_again" with input (filename) as the value
file_again = raw_input("> ")

#defines new variable "txt_again" with read of "file_again" as value
txt_again = open(file_again)
#reads and prints "txt_again"
print txt_again.read()
txt_again.close()
