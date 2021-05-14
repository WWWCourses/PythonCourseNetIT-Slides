import threading
import time



def suma(r):
  global result
  tid = threading.current_thread().name;
  print("{} is working with {}".format(tid, r))

  res = 0
  for i in r:
    res += i

  result += res



# sequential processing:
t = time.time()
result = 0
suma(range(100_000_000))
print(result)
print("Sequential Processing took: ", time.time() - t)


# threaded processing:
t = time.time()
result = 0
tr1 = threading.Thread(target=suma, args=(range(5_000_000),))
tr2 = threading.Thread(target=suma, args=(range(5_000_000,100_000_000 ),))

tr1.start()
tr2.start()

tr1.join()
tr2.join()

print(result)
print("Threaded Processing took: ", time.time() - t)





