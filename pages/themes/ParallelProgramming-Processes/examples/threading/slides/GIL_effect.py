import threading
import time

def worker(r):
  tid = threading.currentThread().name

  # do some hard and time consuming work:
  global result
  res = 0

  for i in r:
    res += i

  result += res
  print("Worker {} is working with {}".format(tid, r))


#################################################
# Sequential Processing:
#################################################
t = time.time()
result = 0

worker(range(50_000_000))
worker(range(50_000_000,100_000_000))

print("Sequential Processing result: ", result)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()
result = 0

tr1 = threading.Thread(target=worker, args=(range(50_000_000),))
tr2 = threading.Thread(target=worker, args=(range(50_000_000,100_000_000),))

tr1.start();tr2.start()
tr1.join(); tr2.join()

print("Multithreaded Processing result: ", result)
print("Multithreaded Processing took:",time.time() - t,"\n")