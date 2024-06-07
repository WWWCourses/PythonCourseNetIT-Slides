import multiprocessing
import time


def worker(num):
    print(f'Worker {num} starting')
    # Simulate some work
    time.sleep(2)
    print(f'Worker {num} done')

if __name__ == '__main__':
    start = time.time()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f'time: {end-start}')
