import multiprocessing

counter = 0

def increment():
    global counter
    for _ in range(10000):
        counter += 1

def decrement():
    global counter
    for _ in range(10000):
        counter -= 1

if __name__=="__main__":
    p1 = multiprocessing.Process(target=increment)
    p2 = multiprocessing.Process(target=decrement)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(counter)
