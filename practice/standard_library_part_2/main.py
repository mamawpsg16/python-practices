# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#     'yellow'], 'blue']]]

# pprint.pprint(t, width=30)

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""

# print(textwrap.fill(doc, width=40))


# import locale
# print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

# conv = locale.localeconv()          # get a mapping of conventions
# print(conv)
# x = 1234567.8

# print(locale.format_string("%d", x, grouping=True))

# print(locale.format_string("%s%.*f", (conv['currency_symbol'],
#                      conv['frac_digits'], x), grouping=True))

# Templating - Writing $$ creates a single escaped $:
# from string import Template
# t = Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))

# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# print(t.substitute(d)) #ERROR AS THERE IS NO ITEM KEYWORD ARGUMENT VARIABLE
# print(t.safe_substitute(d)) # TO NOT RAISE ERROR AND DISPLAY THE ARGUMENT VARIABLE AS IT IS

# import time, os.path
# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# class BatchRename(Template):
#     delimiter = '%'

# fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

# t = BatchRename(fmt)
# # print(t)
# date = time.strftime('%d%b%y')
# # print(date)
# for i, filename in enumerate(photofiles):
#     # print(i, filename, "i, filename") 
#     base, ext = os.path.splitext(filename)
#     # print(os.path.splitext(filename),"os.path.splitext(filename)")
#     # print(base, ext, "base, ext") 
#     newname = t.substitute(d=date, n=i, f=ext)
#     # print(newname,"newname")
#     print('{0} --> {1}'.format(filename, newname),"AWAFAWF")


# Multi-threading
import threading, time, zipfile

# DEFINING THREADING IN CLASS METHODS
class Human:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()  # A lock to synchronize access

    def walk(self):
        with self.lock:
            time.sleep(2)
            print(f"{self.name} finished walking")

    def eating(self):
        with self.lock:
            time.sleep(4)
            print(f"{self.name} finished eating")

    def driving(self):
        with self.lock:
            time.sleep(5)
            print(f"{self.name} finished driving")

    def start_threads(self):
        walk_thread = threading.Thread(target=self.walk)
        eating_thread = threading.Thread(target=self.eating)
        driving_thread = threading.Thread(target=self.driving)

        walk_thread.start()
        eating_thread.start()
        driving_thread.start()

        return walk_thread, eating_thread, driving_thread

person1 = Human("Kevin")

# INITIALIZE THREADING
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)


# def running():
#     time.sleep(3)
#     print("finished running")

# def swimming():
#     time.sleep(5)
#     print("finished swimming")

# def journaling():
#     time.sleep(7)
#     print("finished journaling")

# def thread3():
#     running_thread = threading.Thread(target=running)
#     swimming_thread = threading.Thread(target=swimming)
#     journaling_thread = threading.Thread(target=journaling)
#     journaling_thread.start()
#     swimming_thread.start()
#     running_thread.start()
#     print("THIS WILL RUN FIRST BECAUSE WE DONT WAIT FOR THREADS TO BE FINISHED")

#     journaling_thread.join()
#     swimming_thread.join()
#     running_thread.join()
#     print("THIS WILL RUN AFTER BECAUSE WE NOW WAIT FOR THREADS TO BE FINISHED")

# Logging
# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# Weak References
# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)

# a = A(10)                   # create a reference
# print(a)
# d = weakref.WeakValueDictionary()
# print(d)
# d['primary'] = a            # does not create a reference
# print(d['primary']) # fetch the object if it is still alive

# del a                       # remove the one reference
# # print(d['primary']) # ERROR
# gc.collect()                # run garbage collection right away    

# Tools for Working with Lists  

# from array import array
# a = array('H', [4000, 10, 700, 22222])
# print(sum(a))
# print(a[1:3])
# print(type(a))

# from collections import deque
# d = deque([1, 2, 3])
# d.append(4)
# print("Collection", d)
# print("Handling", d.popleft())

# print([item * 2 for item in d if item % 2 == 0],"NEW")
 
# import bisect # for manipulating sorted lists
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)

# from heapq import heapify, heappop, heappush # The lowest valued entry is always kept at position zero
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)                      # rearrange the list into heap order
# heappush(data, -5)                 # add a new entry
# print([heappop(data) for _ in range(3)])

# Decimal Floating-Point Arithmetic

# from decimal import *
# print(round(Decimal('0.70') * Decimal('1.05'), 2))
# print(round(.70 * 1.05, 2))

# print(Decimal('1.00') % Decimal('.10'))
# print(1.00 % 0.10)
# print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
# print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)
# getcontext().prec = 36
# print(Decimal(1) / Decimal(7))

def main():
    #THREADING EXAMPLE # 1
    # background = AsyncZip('file.txt', 'mytextarchive.zip')
    # background.start() # starts the thread, which in turn calls the run() method in a separate thread of execution.
    # print('The main program continues to run in foreground.')

    # background.join()    # Wait for the background task to finish
    # print('Main program waited until background was done.')

    #THREADING EXAMPLE # 2
    # person = Human("John")
    # threads = person.start_threads()
    # # Optional: Wait for all threads to finish
    # for thread in threads:
    #     thread.join()
    # print("PRINT THIS AFTER THREAD")

    #THREADING EXAMPLE # 3
    # thread3()
    pass


if __name__ == '__main__':
    main()