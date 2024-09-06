import os
# print(os.getcwd()) # Return the current working directory

# os.chdir(f"{os.getcwd()+"/changed_dir"}")   # Change current working directory

# print(os.listdir()) # Return all files within the current directory

# arr = os.listdir('c:\\files') # TO DEFINE THE PATH

# os.system('mkdir today') #  # Run the command mkdir in the system shell

# print(dir(os)) # returns a list of all module functions

# import shutil
# help(shutil) # returns an extensive manual page created from the module's docstrings

# print(dir(shutil)) # returns a list of all module functions

# shutil.copyfile('file.txt', 'copy_file.txt') # COPY FILE to NEW FILE

# shutil.move('copy_file.txt', 'moved_files') # MOVE FILE TO ANOTHER DIRECTORY

# /** File Wildcards */
# import glob # Use glob to find files in the specified directory
# print(glob.glob('C:/Users/kevin.mensah/Desktop/python/moved_files/*.txt')) 

# String Pattern Matching
import re
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# print('tea for too'.replace('too', 'two'))

# Mathematics
# import math
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.random()) # random float
# print(random.randrange(6))    # random integer chosen from range(6)

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))


# Internet Access
# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip()) 

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()

# Dates and Times
# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age)
# print(age.days)

# Data Compression
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# Performance Measurement
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()