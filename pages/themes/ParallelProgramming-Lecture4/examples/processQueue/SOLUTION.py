import multiprocessing as mp
import time

def worker(r):
	pid = mp.current_process().name

	# do some hard and time consuming work:
	global result
	res = 0

	for i in r:
		res += i

	if "Process-" in pid:
		output.put(result)
	else:
		result += res


	print("Worker {} is working with {}".format(pid, r))


if __name__ == '__main__':
	max_range = 1_000_000
	max_range_half = max_range//2

	result = 0

	# Define an output queue
	output = mp.Queue()

	p1 = mp.Process(target=worker, args=(range(0, max_range_half),))
	p2 = mp.Process(target=worker, args=(range(0, max_range_half),))

	p1.start();p2.start()
	p1.join(); p2.join()

	print("Multiprocess Processing result: ", output.get())
