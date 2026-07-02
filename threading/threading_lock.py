import threading

counter = 0
lock = threading.Lock()


def increment(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


if __name__ == "__main__":
    threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Final counter: {counter}")   # 5000 (not random without lock)
