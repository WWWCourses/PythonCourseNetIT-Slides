import threading
import time


def worker(x):
  tid = threading.currentThread().name;
  print("x = {} in {}".format(x, tid))
  time.sleep(5)

# create the tread
tr = threading.Thread(target=worker, args=(42,))

# start the thread:
tr.start()

# wait until thread terminates:
tr.join()

print("Worker did its job!")