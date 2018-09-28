fileWrite = open('sample.txt', 'w')
#    we actually need to create two file objects one for writing file and one for reading it
fileWrite.write("we're gonna write some stuff here\n")
fileWrite.write("hey there everyone\n")
fileWrite.write("saurabh here\n")
fileWrite.write("now i'm gonna close this file")
fileWrite.close()
#reading from a file
fileRead = open('sample.txt', 'r')
readText = fileRead.read()

print(readText)
fileRead.close()

# appending to a file
appendMe = open('sample.txt', 'a')
appendMe.write("\n New bit of information")
appendMe.close()
