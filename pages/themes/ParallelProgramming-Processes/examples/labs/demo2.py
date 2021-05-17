import threading
import time

def worker(r):
  tid = threading.currentThread().name

  # do some hard and time consuming work:
  res = 0

  for i in r:
    res += i

  print("Worker {} is working with {}".format(tid, r))
  return res


#################################################
# Sequential Processing:
#################################################
t = time.time()
result = 0

res1 = worker(range(1_000_000))
res2 = worker(range(1_000_000,10_000_000))

print(f"sum = {res1+res2}")

print("Sequential Processing result: ", result)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()
result = 0

tr1 = threading.Thread(target=worker, args=(range(1_000_000),))
tr2 = threading.Thread(target=worker, args=(range(1_000_000,10_000_000),))

tr1.start();tr2.start()

tr1.join()
tr2.join()



print("Multithreaded Processing result: ", result)
print("Multithreaded Processing took:",time.time() - t,"\n")