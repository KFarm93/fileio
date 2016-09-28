from sys import argv

script, file_to_count = argv

readFile = open(file_to_count)
fileLines = readFile.readlines()
print len(fileLines)
