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

        driving_thread.join()
        eating_thread.join()
        walk_thread.join()

        return walk_thread, eating_thread, driving_thread



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


def running():
    time.sleep(3)
    print("finished running")

def swimming():
    time.sleep(5)
    print("finished swimming")

def journaling():
    time.sleep(7)
    print("finished journaling")

def thread3():
    print("THIS WILL RUN FIRST BECAUSE WE DONT WAIT FOR THREADS TO BE FINISHED")
    running_thread = threading.Thread(target=running)
    running_thread.start()
    swimming_thread = threading.Thread(target=swimming)
    swimming_thread.start()
    journaling_thread = threading.Thread(target=journaling)
    journaling_thread.start()

    # journaling_thread.join()
    # swimming_thread.join()
    # running_thread.join()
    print("THIS WILL RUN AFTER BECAUSE WE NOW WAIT FOR THREADS TO BE FINISHED")

def walk_dog():
    time.sleep(8)
    print("Walk Dog")

def take_out_trash():
    time.sleep(2)
    print("Takeout trash")
    
def get_mail():
    time.sleep(4)
    print("Get mail")

def main():
    # person1 = Human("Kevin")
    # person1.start_threads()
    thread3()
    # chore1 = threading.Thread(target=walk_dog)
    # chore1.start()
    # chore2 = threading.Thread(target=take_out_trash)
    # chore2.start()
    # chore3 = threading.Thread(target=get_mail)
    # chore3.start()
if __name__ == '__main__':
    main()