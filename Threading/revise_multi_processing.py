import time
import multiprocessing

import time
def calculateSquare(nums, shared_variable):
    print("Calculating Square . . . ")
    for idx, n in enumerate(nums):
        shared_variable[idx] = n*n
        time.sleep(0.1)
        print(f"Square of {n} is ", n*n )

def calculateQube(nums, shared_variable):
    print("Calculating Qube . . . ")
    for idx, n in enumerate(nums):
        shared_variable[idx] = n*n*n
        time.sleep(0.1)
        print(f"Qube of {n} is ", n*n*n )

nums = [1,2]
if __name__ == '__main__':
    shared_variable = multiprocessing.Array('i', 2)
    p1 = multiprocessing.Process(target=calculateSquare, args=(nums, shared_variable, ))
    p2 = multiprocessing.Process(target=calculateQube, args=(nums,shared_variable, ))

    print("Unshared nums: ", nums[:])
    print(f"\n shared variables: ", shared_variable[:] )
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"\n shared variables: ", shared_variable[:] )