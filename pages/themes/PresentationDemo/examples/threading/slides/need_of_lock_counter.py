import threading
import time


def worker():
  global counter

  tmp = counter
  print("Before:",counter)
  counter = tmp + 1
  print("After:",counter)



counter = 0

# create some treads to count together:
thread_pool = []
for i in range(10000):
  tr = threading.Thread(target=worker)
  tr.start()
  thread_pool.append(tr)

# wait for tread to finish:
for tr in thread_pool:
  tr.join()

print("Workers counted:", counter)
