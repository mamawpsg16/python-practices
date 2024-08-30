# Syntax Errors
# while True print('Hello world') # invalid syntax

# Exceptions
# print(10 * (1/0))  # ZeroDivisionError: division by zero
# print(4 + spam*3) # NameError: name 'spam' is not defined
# print('2' + 2) # TypeError: can only concatenate str (not "int") to str

# Handling Exceptions
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [C, D, B,]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
print(Exception("AYO"))

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst), "type(inst)")    # the exception type
    print(inst.args, "inst.args")     # arguments stored in .args
    print(inst, "inst")          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


import sys, os

try:
    f = open(os.getcwd()+'\\file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

def this_fails():
    return 1 + 1

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
else:
    print("Success")
finally:
    print('Goodbye, world!')
try:
    raise NameError("SHEESH")
except NameError:
    print('An exception flew by!')
    raise # RAISE THE SHEESH ABOVE

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")