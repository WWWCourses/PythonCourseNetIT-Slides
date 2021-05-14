import multiprocessing

print(multiprocessing.cpu_count())

pool = multiprocessing.Pool()
print(pool._processes)