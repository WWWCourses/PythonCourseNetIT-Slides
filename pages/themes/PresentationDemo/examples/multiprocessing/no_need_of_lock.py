import multiprocessing as mp
import time


def worker():
  global counter

  tmp = output.get()
  print("Before:",tmp)
  counter = tmp + 1
  print("After:",counter)
  output.put(counter)



output = mp.Queue()
output.put(0)



processes = []
# create some processes to count together:
for i in range(100):
  pr = mp.Process(target=worker)
  pr.start()
  processes.append(pr)

# wait for processes to finish:
for pr in thread_pool:
  pr.join()

print("Workers counted:", counter)

