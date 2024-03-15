#!/usr/bin/python
"""
Simple module defining concurrent programming with threads
"""
import time
import concurrent.futures
import requests

start = time.perf_counter()



def do_something(seconds):
    print(f"Sleeping {seconds} second(s) ... ")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)


end = time.perf_counter()
print(f"Elapsed time is : {end - start :.2f} seconds")
