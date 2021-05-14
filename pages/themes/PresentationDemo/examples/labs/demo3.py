import threading
import time


def worker():
  global counter



  tmp = counter
  lock.release()
  print("Before:",counter)

  lock.acquire()
  time.sleep(0.05)
  counter = tmp + 1


  print("After:",counter)




counter = 0

# create a lock
lock = threading.Lock()

# create some treads to count together:
thread_pool = []
for i in range(100):
  tr = threading.Thread(target=worker)
  tr.start()
  thread_pool.append(tr)

# wait for tread to finish:
for tr in thread_pool:
  tr.join()

print("Workers counted:", counter)