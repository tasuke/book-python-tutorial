import sys
import os 
import time

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def elaplsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time()-st}')
        return v
    return wrapper

@elaplsed_time
def get_sequential(nums):
    for num in nums:
        print(fibonacci(num))

@elaplsed_time
def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())

@elaplsed_time
def get_multi_thread(nums):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())

def fibonacci(n):
    a, b = 0,1
    for _ in range(n):
        a, b = b, b+a
    return a
        
def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    print(f'os.cpu_count()={os.cpu_count()}')
    # get_sequential(nums)
    # get_multi_process(nums)
    get_multi_thread(nums)

if __name__ == "__main__":
    main()