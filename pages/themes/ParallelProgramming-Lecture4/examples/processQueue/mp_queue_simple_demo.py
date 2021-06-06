import multiprocessing as mp

def worker(q):
    # get data from queue:
    x = q.get()

    x+=1

    # save data to the queue
    q.put(x)
    print(f'x in {mp.current_process().name} = {x}')




if __name__ == '__main__':
	# create a Queue object which will be shared among all processes
    queue = mp.Queue()

    # set the initial value for queue
    queue.put(0)

    processes = []

    # crate and start 3 processes:
    for _ in range(3):
        pr = mp.Process(target=worker, args=(queue,))
        pr.start()
        processes.append(pr)

    # wait for processes to end:
    for pr in processes:
        pr.join()

    # get element from queue:
    x = queue.get()

    print(f'x in {mp.current_process().name} = {x}')
