import threading
import time

def add(r):
  global result
  res = 0
  for i in r:
    res += i

  result += res
  threadName = threading.current_thread().name

#################################################
# Sequential Processing:
#################################################
t = time.time()
result = 0

worker(range(500_000))
worker(range(500_000,1_000_000))

print("Sequential Processing result: ", result)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()
result = 0

#create threads
tr1 = threading.Thread(name="tr1", target=add, args=(range(50_000_00),))
tr2 = threading.Thread(name="tr2", target=add, args=(range(50_000_00,100_000_00),))


# start threads
tr1.start(); tr2.start()

# wait threads to finish their job
tr1.join(); tr2.join()

print("Multithreaded Processing result: ", result)
print("Multithreaded Processing took:",time.time() - t,"\n")