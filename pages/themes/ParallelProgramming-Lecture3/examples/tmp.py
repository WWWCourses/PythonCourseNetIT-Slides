import threading

def worker():
	global counter

	# lock the 'critical section':
	lock.acquire()
	for i in range(1_000_000):
		counter += 1
	lock.release()


counter = 0
lock = threading.Lock()

# create some treads to count together:
thread_pool = []
for i in range(5):
	tr = threading.Thread(target=worker)
	thread_pool.append(tr)

	print(f"Counter before start of {tr.name}: {counter}")
	tr.start()

# wait for tread to finish:
for tr in thread_pool:
	tr.join()

print("Workers counted:", counter)