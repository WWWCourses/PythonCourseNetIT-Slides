import multiprocessing as mp
import time

def worker(x):
  tid = mp.current_process().name

  # do some hard and time consuming work:
  time.sleep(1)
  print("Process {} is working with {}".format(tid, x))


#################################################
# Sequential Processing:
#################################################
t = time.time()
worker(42)
worker(84)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()
p1 = mp.Process(target=worker, args=(42,))
p2 = mp.Process(target=worker, args=(82,))

p1.start();p2.start()
p1.join(); p2.join()
print("Multithreaded Processing took:",time.time() - t)