def log_timer(original_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time()
        print(f'{original_func.__name__} ran in {t2 - t1} seconds.')
    return wrapper

@log_timer
def display():
    import time
    print('my func started running.')
    time.sleep(1)
    print('my func stopped working')



display()