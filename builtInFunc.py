print(abs (-1)) 

#   built in all()
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True         #   return true if the the argument is iteratable or it is a string

print(all('saurabh'))

#   built in any()
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False 

print(any(''))  # what the fuck!

# the main diff b/w repr() and str() is that str() is used for end user side, where as repr() is used for debugging or development purposes.
import datetime
today = datetime.datetime.now()
print(repr(today))
print(str(today))

#   complex numeric values
z = complex(3,4)
print(str(z))

n = 37
print(bin(n))   # used to print binary of integer
print(n.bit_length())


print((1024).to_bytes(2, byteorder='big'))

print('{:*^50}'.format('    centered    '))
points = 7
total = 10
print('correct answers: {:.3%}'.format(points/total))

