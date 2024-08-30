# LISTS
list_data = [1, 2, 3]

list_data.append(4) # = a[len(a):] = [x]

list_data.extend([5,6]) # = list_data[len(list_data):] = [5,6]

list_data.insert(0, 7)

list_data.remove(7) #REMOVE THE EQUAL ITEM 

popped_data = list_data.pop(1)
print(f"{popped_data} popped_data")

# list_data.clear() #clear list

index = list_data.index(3)
print(f"{index} index")

list_data.append(4)
no_of_occurence = list_data.count(4)
print(f"{no_of_occurence} no_of_occurence")

list_data.sort()
print(f"{list_data} list_data")

words = ["apple", "banananas", "cherry"]
words.sort(key=len)  # Sorts words by length
print(f"{words} sort words by length")

newWords = words.copy()
newWords[0] = 'HALLELUJAH'
print(f"{newWords} newWords")

# Using Lists as Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves


# List Comprehensions #A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
squares = []
for x in range(10):
    squares.append(x**2)
print(f"{squares} squares")

squaresV1= list(map(lambda x:x**2, range(10)))
print(f"{squaresV1} squaresV1")

squaresV2 = [x**2 for x in range(10)]
print(f"{squaresV2} squaresV1")

list_of_tuples = [(x,y) for x in [1,2,3] for y in [3,1,3] if x != y ]
print(f"{list_of_tuples} list_of_tuples")

vec = [-4, -2, 0, 2, 4]
doubled_vec = [x*2 for x in vec]# create a new list with the values doubled
positive_vec = [x*2 for x in vec if x >= 0]# filter the list to exclude negative numbers
absolute_vec = [abs(x) for x in vec]# apply a function to all the elements
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped_weapons = [weapon.strip() for weapon in freshfruit] #call a method on each element
print(f"{stripped_weapons} stripped_weapons")

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
flatten_vec = [y for elem in vec for y in elem]
print(f"{flatten_vec} flatten_vec")

#complex nested functions from math import pi
from math import pi
nested_functions = [str(round(pi, i)) for i in range(1, 6)]
print(f"{nested_functions} nested_functions")


#Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrixV1 = [5,6,7,8]

rows_columns = [[row[i] for row in matrix] for i in range(4)]
#EQUALS TO THIS 
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(f"{transposed} transposed")

#The zip() function would do a great job for this use case:
two_d_matrix_zipped = list(zip(*matrix))
print(f"{two_d_matrix_zipped} two_d_matrix_zipped")

# del statement
nums = [-1, 1, 66.25, 333, 333, 1234.5]
del nums[0]
print(f"{nums} nums")


# Tuples and Sequences  - A tuple consists of a number of values separated by commas, for instance:
tup = 12345, 54321, 'hello!'
print(f"{tup} tup")
# Tuples may be nested:
nested_tupples = tup, (1, 2, 3, 4, 5)
print(f"{nested_tupples} nested_tupples")
# Tuples are immutable:
# t[0] = 88888 # ERROR 

# but they can contain mutable objects:
tupple_with_lists = ([1, 2, 3], [3, 2, 1])
print(f"{tupple_with_lists} tupple_with_lists")

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(singleton)
a,b,c = tup # Sequence unpacking TUPLE - requires that there are as many variables on the left side of the equals sign as there are elements in the sequence
print(a,b,c, "a,b,c")

# SETS 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   
print('orange' in basket )
print('crabgrass' in basket)
a = set('abracadabra')
b = set('alacazam')
print(f"{a} a")
print(f"{b} b")
print(a - b, "letters in a but not in b") # letters in a but not in b
print(a | b, "letters in a or b or both" ) # letters in a or b or both
print(a & b, "letters in both a and b") # letters in both a and b
print(a ^ b, "letters in a or b but not both") # letters in a or b but not both

a1 = {x for x in 'abracadabra' if x not in 'abc'}
print(a1)

# DICTIONARIES
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 #MUTATE OF EXISTING KEY VALUE 

del tel['sape'] #DELETE KEY VALUE PAIR
tel['irv'] = 4127 #ADD NEW KEY VALUE PAIR IF NOT EXISTS
print(f"{tel} tel")
print(f"{list(tel)} TEL KEYS")
print('guido' in tel, "'guido' in tel")
print('jack' not in tel, " 'jack' not in tel")

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dictionary_details = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(f"{dictionary_details} dictionary_details")

# dict comprehensions
print({x: x**2 for x in (2, 4, 6)})

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098))

# Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print("ZIP", list(zip(questions, answers)))
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)

basketv1 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basketv1):
    print(i)

#Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() 
#over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

basketv2 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basketv2)):
    print(f, "basket v2")

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data,"filtered_data")


# Add the parent directory of 'test_modules' to the Python path
import sys
sys.path.insert(0,r'C:\Users\kevin.mensah\Desktop\python') # INSERT PATH INTO BEGINNING OF SYS.PATH
sys.path.append(r'C:\Users\kevin.mensah\Desktop\python') # APPEND PATH TO END OF SYS.PATH

from test_modules import test
print(test.test())