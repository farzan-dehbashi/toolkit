import threading
import time
resource = []

def task1():
    for i in range(10):
        time.sleep(0.1)


def task2():
    for i in range(10):
        time.sleep(0.1)


if __name__ == '__main__':

    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()

