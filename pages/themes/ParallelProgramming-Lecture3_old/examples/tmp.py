import requests
import os
import time


start_time = time.time()
time.sleep(1)
print(time.time() - start_time)

start_pcounter = time.perf_counter()
time.sleep(1)
print(time.perf_counter() - start_pcounter)