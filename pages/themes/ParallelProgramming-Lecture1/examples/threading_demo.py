import threading
import time


def worker(num):
    print(f'Worker {num} starting')
    # Simulate some work
    time.sleep(2)
    print(f'Worker {num} done')

if __name__ == '__main__':
    start = time.time()
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f'time: {end-start}')
