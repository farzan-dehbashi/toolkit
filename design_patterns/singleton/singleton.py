class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = None


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s1.value = 42
    print(s2.value)       # 42 — same instance
    print(s1 is s2)       # True
