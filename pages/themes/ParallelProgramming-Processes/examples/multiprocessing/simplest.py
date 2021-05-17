import multiprocessing as mp
import time


def worker(x):
  pid = mp.current_process().name;
  print("x = {} in {}".format(x, pid))
  time.sleep(2)


if __name__ == '__main__':
  # create the process
  p = mp.Process(target=worker, args=(42,))

  # start the process:
  p.start()

  # wait until process completes:
  p.join()

  print("Worker did its job as separate Process!")
