import threading
from datetime import datetime
from time import sleep

def countdown(counter, delay):
    tr_name = threading.current_thread().name
    while counter:
        curr_time = datetime.now().strftime('%H:%M:%S')
        print("{:10s}: {:s}".format(tr_name, curr_time))
        sleep(delay)
        counter -= 1

class CountdownThread(threading.Thread):
    def __init__(self, name, delay, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        countdown(self.counter, self.delay)
        print(f"\nExiting {self.name}")

# Create new threads
counter1 = CountdownThread("Counter-1", delay=1, counter=2)
counter2 = CountdownThread("Counter-2", delay=1, counter=3)

# Start new Threads
counter1.start()
counter2.start()

# Join new threads
counter1.join()
counter2.join()

print(f"\nExiting Main Thread")
