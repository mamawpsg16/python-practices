# Fancier Output Formatting
yes_votes = 42_572_654_00_00
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:,.2f} YES votes  {:2.2%}'.format(yes_votes, percentage))
print('{:,.2f} YES votes  {:1.1%}'.format(yes_votes, percentage))
print('{:d}'.format(123))
print('{:,}'.format(1000000))
print('{:010d}'.format(42))
print('{:1>10d}'.format(42))
print('{:->10d}'.format(42))
# < for left-align.
# > for right-align.
# ^ for center-align.

s = 'Hello, world.'
print(str(s))
print(repr(s))
x = 10 * 3.25
y = 200 * 200
print(repr((x, y, ('spam', 'eggs'))))



# formatted string literals -  
# - begin a string with f or F before the opening quotation mark or triple quotation mark. 
# - you can write a Python expression between { and } characters that can refer to variables or literal values.
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

import math
print(f'The value of pi is approximately {math.pi:.3f}.') #   three places after the decimal
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# The String format() Method
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# POSITIONAL ARGUMENT
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# KEYWORD ARGUMENT
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# POSITIONAL AND KEYWORD ARGUMENT COMBINED
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

table2 = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table2))
print('{:3d}'.format(42)) # MINIMUM OF 3 CHARACTERS

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# Manual String Formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ') # rjust RIGHT JUSTIFY 
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

print('12'.zfill(5))
print('-3.14'.zfill(7))

#  Old string formatting
import math
from os import getcwd
print('The value of pi is approximately %5.3f.' % math.pi)

print(getcwd()+'\\file.txt')
# Reading and Writing Files
# with open(getcwd()+'\\file.txt', encoding="utf-8") as f:
# with open(r'C:\Users\kevin.mensah\Desktop\python\file.txt', 'w', encoding="utf-8") as f:
# with open(r'C:\Users\kevin.mensah\Desktop\python\file.txt', 'rb+') as f:
    # READ FILE
    # read_data = f.read() # read entire file
    # print(read_data, "read_data")
    # read_line = f.readline() # read line
    # print(read_line, end=" ",)
    # for line in f: # you can loop over the file object
    #     print(line, end='')

    #WRITE IN FILE
    # f.write('This is a test\n')
    # value = ('the answer', 42)
    # s = str(value)  # convert the tuple to string
    # f.write(s)

    # f.write(b'0123456789abcdef')
    # print( f.seek(5))
    # print(f.read(1))
    # print(f.seek(-3, 2))

# We can check that the file has been automatically closed.
# print(f.closed)

#Saving structured data with json
    
import json
x = [1, 'simple', 'list']
print(type(x))
print(json.dumps(x))

# with open(r'C:\Users\kevin.mensah\Desktop\python\file.txt', 'w', encoding="utf-8") as f:
#     json.dump(x, f)

# with open(r'C:\Users\kevin.mensah\Desktop\python\file.txt', 'r', encoding="utf-8") as f:
#     data = json.load(f)  # Load JSON data from the file
    # print(type(data))  # Print the decoded JSON data