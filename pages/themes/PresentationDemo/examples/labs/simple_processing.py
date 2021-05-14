import multiprocessing as mp
import time



def suma(r):
  pid = mp.current_process().name;
  print("{} is working with {}".format(pid, r))

  res = q.get()
  for i in r:
    res += i

  q.put(res)


if __name__ == '__main__':
  # sequential processing:
  t = time.time()
  result = 0
  suma(range(100_000_000))
  print(result)
  print("Sequential Processing took: ", time.time() - t)


  # multi-processes processing:
  t = time.time()
  q = mp.Queue()

  q.put(0)
  pr1 = mp.Process(target=suma, args=(range(5_000_000),))
  pr2 = mp.Process(target=suma, args=(range(5_000_000,100_000_000 ),))

  pr1.start()
  pr2.start()

  pr1.join()
  pr2.join()

  print(result)
  print("Threaded Processing took: ", time.time() - t)





