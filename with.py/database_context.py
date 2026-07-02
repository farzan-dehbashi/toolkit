import sqlite3


class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
        return False


class Timer:
    import time

    def __enter__(self):
        import time
        self._start = time.time()
        return self

    def __exit__(self, *args):
        import time
        self.elapsed = time.time() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")


if __name__ == "__main__":
    with Timer() as t:
        total = sum(range(1_000_000))
    print(f"Sum: {total}")
