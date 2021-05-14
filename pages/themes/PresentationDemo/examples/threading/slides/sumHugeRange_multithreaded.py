import threading
import time

def worker(r):
  global result
  res = 0

  for i in r:
    res += i

  result += res



#################################################
# Multithreaded Processing:
#################################################
t = time.time()
result = 0

#create threads
tr1 = threading.Thread(name="tr1", target=worker, args=(range(500_000),))
tr2 = threading.Thread(name="tr2", target=worker, args=(range(500_000,1_000_000),))


# start threads
tr1.start(); tr2.start()

# wait threads to finish their job
tr1.join(); tr2.join()

print("Multithreaded Processing result: ", result)
print("Multithreaded Processing took:",time.time() - t,"\n")