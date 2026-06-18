from threading import Thread
from multiprocessing import process
import time
def calculateSquare(nums):
    print("Calculating Square . . . ")
    for n in nums:
        time.sleep(0.1)
        print(f"Square of {n} is ", n*n )

def calculateQube(nums):
    print("Calculating Qube . . . ")
    for n in nums:
        time.sleep(0.1)
        print(f"Qube of {n} is ", n*n*n )

nums = [1,2,3,4,5]
t1 = Thread(target=calculateSquare, args=(nums,))
t2 = Thread(target=calculateQube, args = (nums, ))

t1.start()
t2.start()
t2.join()
t2.join()