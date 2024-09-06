# A context manager implements two special methods:

# __enter__(self): This method is executed when the with block is entered. It can set up resources and return an object that can be used within the block.
# __exit__(self, exc_type, exc_value, traceback): This method is executed when the with block is exited, whether normally or due to an exception. It handles cleanup actions.

# EXAMPLE 1 
# with open('file.txt', 'r') as file:
#     content = file.read()
# File is automatically closed here, even if an exception occurs

# Class-based Context Manager
class MyContextManager:
    def __enter__(self):
        print('Entering context')
        return self  # Optional: return any value you want to use in the block

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting context')
        # Optionally handle exceptions
        return False  # Propagate exceptions, return True to suppress them

# with MyContextManager() as manager:
#     print('Inside context')


# Function-based Context Manager (using contextlib)
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print('Entering context')
    try:
        yield "Kevin" # Optional: yield any value you want to use in the block
    finally:
        print('Exiting context')

# with my_context_manager() as value:
#     print('Inside context')
#     print('Value', value)


# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1

# for number in count_up_to(5):
#     print(number)