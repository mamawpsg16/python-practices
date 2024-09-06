#  using a with statement is that it makes sure our file is closed without paying attention to how the nested block exits.
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

filename = 'file.txt'
file_path = os.path.join(BASE_DIR, filename)

# Implementing a Context Manager in a Function
def file_example_cm():
    with open(file_path, 'w') as opened_file:
        opened_file.write('Hola!')

    # ABOVE EQUIVALENT TO 
    # file = open(file_path, 'w')
    # try:
    #     file.write('Hola!')
    # finally:
    #     file.close()
        
# Implementing a Context Manager as a Class
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        return True # Our __exit__ method returned True, therefore no exception was raised by the with statement

# Implementing a Context Manager as a Generator
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

def main():
    # file_example_cm()

    # CORRECT 
    # with File(file_path, 'w') as opened_file:
    #     opened_file.write('Hola v2!')

    # ERROR
    # with File(file_path, 'w') as opened_file:
    #     opened_file.undefined_function('Hola!')

    # with open_file(file_path) as f:
    #     f.write('hola!')

if __name__ == '__main__':
    main()