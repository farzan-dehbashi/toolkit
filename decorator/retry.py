import time
import functools


def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


if __name__ == "__main__":
    call_count = 0

    @retry(max_attempts=3, delay=0)
    def flaky_function():
        global call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("Not ready yet")
        return "success"

    print(flaky_function())   # succeeds on 3rd attempt
