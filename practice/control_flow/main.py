# x = int(input("Please enter an integer: "))
#IF STATEMENT
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#FOR STATEMENT
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy

# Without copy(): You'll encounter runtime errors or unexpected behavior if you try to modify the dictionary during iteration.
for user, status in users.copy().items(): 
    if status == 'inactive':
        del users[user]
print(f"{users} users 2")

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(f"{active_users} active_users")

#Range function
# for i in range(5):
for i in range(5, 10):
    print(i)

rangeList = list(range(5, 10))#create a list base on range
print(f"{rangeList}, rangeList")
negativeRangeList = list(range(-10, -100, -30))#create a list base on range
print(f"{negativeRangeList}, negativeRangeList")

#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i], end=",")

#USE ENUMERATE FOR HAVING THE INDEX OF ITEM
seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 
enumaratedSeason = list(enumerate(seasons)) 
enumaratedSeasonV1 = list(enumerate(seasons, start=1))

for index, season in enumaratedSeason:
    print(index, season)
 
print(range(10))
print(sum(range(4)))

# Break and continue Statements, and else Clauses on Loops
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(f"{i} is equals {j} * ", i//j)
            break
    else:
        print(f"{i} is a prime number")


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
def initlog(*args):
    pass   # Remember to implement this!

class MyEmptyClass:
    pass

#match statements
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(405))

point = (5, 10)
print(f"{point} point")

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

var1 = 0
var2 = 10
pointOne = Point(0, var1)
pointTwo = Point(0, y=var2)
pointThree = Point(x=1, y=var1)
pointFour = Point(1, 1)
notAPoint = "HAAHAH"
where_is(notAPoint)

class PointV1:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

pointsV1 = []
pointsV2 = [PointV1(0,0)]
pointsV3 = [PointV1(1,2)]
pointsV4 = [PointV1(0,2), PointV1(0,2)]
match pointsV4:
    case []:
        print("No points")
    case [PointV1(0, 0)]:
        print("The origin")
    case [PointV1(x, y)]:
        print(f"Single point {x}, {y}")
    case [PointV1(0, y1), PointV1(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

guardedPoint = PointV1(1, 1)
match guardedPoint:
    case PointV1(x, y) if x == y:
        print(f"Y=X at {x}")
    case PointV1(x, y):
        print("Not on the diagonal")

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color("red")

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

#Defining Functions
def test():
    print("Defined test Function")

test()

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

#Default argument values
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while retries > 0:
#         reply = input(prompt).lower()
#         print(f"{reply} reply")
#         if reply in {'y', 'ye', 'yes'}:
#             print(f"{reply} TRUE")
#             return True
#         elif reply in {'n', 'no', 'nop', 'nope'}:
#             print(f"{reply} FALSE")
#             return False
#         retries -= 1
#         if retries > 0:
#             print(reminder)
#     raise ValueError('invalid user response')
    
# ask_ok("Are you good?")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while retries > 0:
        reply = input(prompt).lower()
        print(f"{reply} reply")
        if reply in {'y', 'ye', 'yes'}:
            print(f"{reply} TRUE")
            retries -= 1
            print(reminder)
        
        elif reply in {'n', 'no', 'nop', 'nope'}:
            print(f"{reply} FALSE")
            return False
    raise ValueError('invalid user response')

# Test the function
# ask_ok("Are you good? ")

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f1(1))
print(f1(2))
print(f1(3))

#Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action)
    print("-- if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#VALID
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=2000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#INVALID
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
    
unpackingList = [1,2,3]
[one, *rest] = unpackingList
print(f"{one, rest} unpackingList")
unpackingTupple = (1,2,3)
[onev1, *restv1] = unpackingList
print(f"{onev1, restv1} unpackingTupple")
unpackingDictionary = {0:1, 1:2, 2:3}
# Unpack dictionary keys and values
(key1, value1), *rest_items = unpackingDictionary.items()

# Convert rest_items back to a dictionary if needed
rest_dict = dict(rest_items)

print(f"First key-value pair: ({key1}: {value1})")
print(f"Rest of the dictionary: {rest_dict}")

#Keyword Arguments in functions
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#Special parameters

def standard_arg(arg):
    print(arg, "POSITION OR KEYWORD")

def pos_only_arg(arg, /):
    print(arg, "POSITION ONLY")

def kwd_only_arg(*, arg):
    print(arg, "KEYWORD ONLY")

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only, "COMBINED ARGUMENTS")

#POSITION OR KEYWORD
standard_arg(2)
standard_arg(arg=2)

#POSITION ONLY
pos_only_arg(1)
# pos_only_arg(arg=1) # ERROR AS IT POSITIONAL ONLY 

#KEYWORD ONLY
# kwd_only_arg(3) # ERROR AS IT KEYWORD ONLY 
kwd_only_arg(arg=3)

#COMBINED EXAMPLE
# combined_example(1, 2, 3) # ERROR AS THE FIRST ARG IS POSITIONAL SECOND IS POSITIONAL OR KEYWORD AND THIRD IS  KEYWORD ONLY 

combined_example(1, 2, kwd_only=3)
combined_example(4, standard=5, kwd_only=6)


def foo(name,/, **kwds):
    print(kwds,"kwds")
    return 'name' in kwds

print(foo("kevin", **{'name':"kevin","age":15})) #dictionary as keyword arguments, you need to use ** when calling the function

#Arbitrary argument lists
def concat(*args, sep="/"):
    print(args,"args")
    return sep.join(args)

fullName = concat("Kevin","Mensah")
petName = concat("Dog","Bruno", sep=" ")
print(fullName)
print(petName)


#Unpacking Argument Lists
list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
print(list(range(*args)))
print(*args)

def parrotV1(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action)
    print("-- if you put", voltage, "volts through it.")
    print("-- E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrotV1(**d)

#Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

x = lambda x,y: x + y
print(x(10,20))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs, "pairs")

#Documentation Strings

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#Function Annotations

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')