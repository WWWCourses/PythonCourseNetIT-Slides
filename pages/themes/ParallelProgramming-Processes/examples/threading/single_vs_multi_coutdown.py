import threading
import time

def countdown(n):
  while n > 0:
    time.sleep(0.02)
    n -= 1

count = 10


# single-thread processing:
tsingle = time.time()
countdown(count)
countdown(count)
print("single-thread time:",time.time() - tsingle,"\n")

# multithreaded processing:
tmulti = time.time()
tr1 = threading.Thread(target=countdown, args=(count,))
tr2 = threading.Thread(target=countdown, args=(count,))
tr1.start()
tr2.start()

tr1.join()
tr2.join()
print("multi-thread time:",time.time() - tmulti)