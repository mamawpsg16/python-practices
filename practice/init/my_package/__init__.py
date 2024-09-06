__all__ = ['test_module1', 'test_module2']

def init_function():
    print("Initializing function")

variable = "Initialized Variable"

from .module1 import test1 as test_module1
from .module2 import test2 as test_module2

print("MY PACKAGE INIT")
