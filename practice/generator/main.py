# GENERATOR = When a generator function like count_up_to(n) is called, it doesn't return a list of numbers all at once. Instead, it returns a generator object, which can be iterated over.
# Each time you request the next value (using next() function or in a for loop), the generator function resumes where it left off, computes the next value, and 
# pauses again. This makes generators more memory-efficient than creating a list of all values at once, especially for large or infinite sequences.

# YIELD =  When a generator's next() method is called, the generator runs until it reaches a yield statement. The value after the yield keyword is returned to the caller,
# but the function is not exited. Instead, the next time next() is called, the function resumes from where it left off, and it continues to the next yield statement, 
# and so on.
def count_up_to(n):
    for i in range(n):
        yield i
        
my_gen = count_up_to(5)
for num in my_gen:
    print(num)