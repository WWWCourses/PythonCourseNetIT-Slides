import threading
import time


def worker():
  global counter

  # lock the critical section

  tmp = counter
  time.sleep(0.03)
  counter = tmp + 1
  #unlock




counter = 0

lock = threading.Lock()

# create some treads to count together:
thread_pool = []
for i in range(10):
  tr = threading.Thread(target=worker)
  tr.start()
  thread_pool.append(tr)

# wait for tread to finish:
for tr in thread_pool:
  tr.join()

print("Workers counted:", counter)