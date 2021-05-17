import threading
import time


def countdown(n, ouptut_file):
  while n > 0:
    n -= 1


def countdown_in_file(n, ouptut_file):
  with open(ouptut_file, "a") as f:
    f.write(threadID+"\n")

    while n > 0:
      n -= 1
      f.write("{}".format(n))

ouptut_file = "countdown.txt"
count = 100_000_000

#################################################
# Sequential Processing:
#################################################
t = time.time()

countdown(count, ouptut_file)
countdown(count, ouptut_file)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()

tr1 = threading.Thread(target=countdown, args=(count,ouptut_file))
tr2 = threading.Thread(target=countdown, args=(count,ouptut_file))

tr1.start();tr2.start()
tr1.join(); tr2.join()
print("Multithreaded Processing took:",time.time() - t)