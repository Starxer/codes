"""
File Name   :cpu_burner
Author      :qylyf
IDE         :PyCharm
Date        :2023/7/30
Description :
---
Change Activity:2023/7/30:
"""
import multiprocessing, time, random
def func(t):
    t1 = time.time()
    while True:
        x = random.random() * random.random()
        t2 = time.time()
        if t2 - t1 > t:
            break


if __name__ == "__main__":
    workers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(workers)

    t = input("运行多久")

    pool.map(func, [float(t)]*workers)

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()
    print("Sub-process(es) done.")