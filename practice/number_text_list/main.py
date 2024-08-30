# COMMENTS
# this is the first comment
spam = 1  # and this is the second comment
        # ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)

# NUMBERS
print((50 - 5*6) / 4) #parentheses (()) can be used for grouping
print(17 // 3) # floor division discards the fractional part
width = 20
print(f"{width} width")

# TEXTS = Python strings cannot be changed — they are immutable.
print('doesn\'t')  # use \' to escape the single quote “escape” it, by preceding it with \
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
print('First line.\nSecond line.')  # \n means newline
#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#multiple lines  prevent the newline in the start  by adding a \
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *
print(3 * 'un' + 'ium')
print('Py' "thon") #Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
#This feature is particularly useful when you want to break long strings: NOTE:::This only works with two literals though, not with variables or expressions:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
#If you want to concatenate variables or a variable and a literal, use +:
prefix = 'Py'
print(prefix + 'thonv1')

#Indexing
word = 'Python'
print(f"{word} - {word[1]} String Index 1")
print(f"{word} - {word[-6]} String Index -6")

#Slicing
print(f"{word} - {word[0:2]} String Sliced 0:2") #Index 2 is Excluded
print(f"{word} - {word[:2]} String Sliced beginning:2")
print(f"{word} - {word[4:]} String Sliced 4:end")
print(f"{word} - {word[-2:]} String Sliced -2:end")
print(f"{word} - {word[:2] + word[2:]} Concatenate using Sliced :2 and 2:")
print(word[4:42],"word[4:42]")
print(word[42:],"word[42:]")
# word[0] = 'J' # ERROR STRING IS IMMUTABLE
print('J' + word[1:])
print(len(word))

#LISTS = 
squares = [1, 4, 9, 16, 25]
print(squares)

#Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(f"{squares} - {squares[0]} Lists Index 0")
print(f"{squares} - {squares[2:]} Lists Index 2:")
print(f"{squares} - {squares[:4]} Lists Index :4") #Index 4 is excluded

#Lists also support operations like concatenation:
print(squares + [36, 49, 64, 81, 100])

#Lists are mutable type
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(f"{cubes} cubes modify")

#Append new item in lists
cubes.append(216)
print(f"{cubes} cubes append")

# When you assign a list to a variable, the variable refers to the existing list
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object

rgba.append("Alph")
print(f"{rgb} RGB")
print(f"{rgba} RGBA")

# Shallow Copy
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(f"{rgba} RGB")
print(f"{correct_rgba} RGBA")

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = ['C', 'D', 'E'] # replace some values
print(f"{letters} replace 2:5") #Exclude index 5


letters[2:5] = [] # now remove them
print(f"{letters} remove 2:5") #Exclude index 5

letters[:] = [] #clear list
print(f"{letters} clear list")

#It is possible to nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(len(x))
print(x[0])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b
    