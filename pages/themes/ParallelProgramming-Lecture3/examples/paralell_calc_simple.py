import multiprocessing as mp
import threading
import time

def calc_sum_seq(start, end):
	for num in range(start, end+1):
		global total_sum
		total_sum+=num
	print(f'Total sum: {total_sum}')

def calc_sum_tr(start, end, lock):
	lock.acquire()
	for num in range(start, end+1):
		global total_sum
		total_sum+=num
	lock.release()
	print(f'Total sum: {total_sum}')

def calc_sum_pr(start, end, queue):
	total_sum = queue.get()
	for num in range(start, end+1):
		total_sum+=num
	queue.put(total_sum)
	print(f'Total sum: {total_sum}')

def calc_sum_pr_pool(start, end):
	total_sum = 0
	for num in range(start, end+1):
		total_sum+=num
	print(f'Total sum: {total_sum}')
	return total_sum

def calc_sequential():
	time_start = time.time()
	calc_sum_seq(START, END)
	time_end = time.time()
	print(f'Sequential Time: {time_end-time_start}')

def calc_threaded():
	time_start = time.time()
	lock = threading.Lock()
	tr1 = threading.Thread(target=calc_sum_tr, args=(START, END//2, lock))
	tr2 = threading.Thread(target=calc_sum_tr, args=(END//2 + 1, END, lock))

	tr1.start(), tr2.start()
	tr1.join(), tr2.join()
	time_end = time.time()
	print(f'Threaded Time: {time_end-time_start}')

def calc_multiprocessing():
	time_start = time.time()
	queue = mp.Queue()
	queue.put(0)

	pr1 = mp.Process(target=calc_sum_pr, args=(START, END//2, queue))
	pr2 = mp.Process(target=calc_sum_pr, args=(END//2 + 1, END, queue))

	pr1.start(), pr2.start()
	pr1.join(), pr2.join()
	time_end = time.time()
	print(f'Multiprocessing Time: {time_end-time_start}')

def calc_multiprocessing_pool():
	time_start = time.time()
	p = mp.Pool(processes=5)
	total_sum_list = p.starmap(calc_sum_pr_pool, ((START, END//2), (END//2 + 1, END)))
	print(f'Total sum: {sum(total_sum_list)}')
	p.close()
	p.join()
	time_end = time.time()
	print(f'Multiprocessing Pool Time: {time_end-time_start}')


if __name__ == '__main__':
	# print main process id:
	main_process = mp.current_process()
	print(f'Main Process: {main_process.name, main_process.pid}')

	START = 1
	END = 1_000_000

	total_sum = 0
	calc_sequential()

	total_sum = 0
	calc_threaded()

	total_sum = 0
	calc_multiprocessing()

	total_sum = 0
	calc_multiprocessing_pool()
