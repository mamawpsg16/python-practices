# Scopes and Namespaces
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


# Class Objects
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    """A simple example class"""
    i = 12345

    def introduction(self):
        return f"Hello Im {self.name} and im {self.age} years old"

person_class = Person("Kevin Mensah", 25)
print(f"Introduction: {person_class.introduction()}")
print("__doc__ :", person_class.__doc__ )

# Instance Objects
max_iterations = 10
iterations = 0
while person_class.age > 20 and iterations < max_iterations:
    person_class.age = person_class.age * 2
    iterations += 1

print(person_class.age)

# Class and Instance Variables
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = [] 

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, "Fido")
print(e.kind, "Buddy")
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks, "Fido tricks")
print(e.tricks, "Buddy tricks")

# Random Remarks
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


# Inheritance
class Animal():
    def walk(self):
        print("Walking...")

    def running(self):
        print("Running...")


class Dog(Animal):
    def __init__(self, name, species):
        self.name = name    # instance variable unique to each instance
        self.species = species 

    # def walk(self):
    #     Animal.walk(self)

dog = Dog("Tyler", "Dog")
dog.walk()
print(f"Dog name: {dog.name}")
print(isinstance(dog, Dog) )  # True, because dog is an instance of Dog
isinstance(dog, Animal)   # True, because Dog is a subclass of Animal
print(issubclass(Dog, Animal) )   # True, because Dog is a subclass of Animal

# Multiple Inheritance

# Define a base class for running
class Running:
    def run(self):
        return "Running at full speed!"

# Define a base class for walking
class Walking:
    def walk(self):
        return "Walking at a steady pace."

# Define a Robot class that inherits from both Running and Walking
class Robot(Running, Walking):
    def __init__(self, name):
        self.name = name
    
    def get_status(self):
        return f"{self.name} is {self.run()} and {self.walk()}"

# Create an instance of Robot
my_robot = Robot("Robo")

# Use the methods from both Running and Walking
print(my_robot.get_status())


# Private Variables
class MyClass:
    def __init__(self, value):
        self._private_variable = value  # This is a private variable

    def get_private_variable(self):
        return self._private_variable

    def set_private_variable(self, value):
        self._private_variable = value

# Example usage
obj = MyClass(10)
print(obj.get_private_variable())  # Output: 10

obj.set_private_variable(20)
print(obj.get_private_variable())  # Output: 20

# Direct access to the private variable is discouraged but possible
print(obj._private_variable)  # Output: 20 (not recommended)


# super()
class Fish:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return "Swim....."

class Tuna(Fish):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__ method
        self.breed = breed

    def speak(self):
        return "BLUBLUBLUB!"

my_fish = Tuna("Buddy", "Organo")

print(my_fish.name)  # Output: Buddy
print(my_fish.breed)  # Output: Golden Retriever
print(my_fish.speak())  # Output: Woof!
print(my_fish.swim())  # Output: Woof!


# Odds and Ends
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
john = Employee('john', 'computer lab', 1000)
print(john.dept)


# Iterators
s = 'abc'
it = iter(s) # the for statement calls iter() on the container objec
print(it)
print(next(it)) # __next__() which accesses elements in the container one at a time.
print(next(it))
print(next(it))

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
print(iter(rev),'rev')
for char in rev:
    print(char)