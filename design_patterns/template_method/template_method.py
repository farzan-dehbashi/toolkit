from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self, data):
        data = self.read(data)
        data = self.transform(data)
        self.write(data)

    @abstractmethod
    def read(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    def write(self, data):
        print(f"Writing: {data}")


class UpperCaseProcessor(DataProcessor):
    def read(self, data):
        print(f"Reading: {data}")
        return data

    def transform(self, data):
        return data.upper()


class ReverseProcessor(DataProcessor):
    def read(self, data):
        print(f"Reading: {data}")
        return data

    def transform(self, data):
        return data[::-1]


if __name__ == "__main__":
    UpperCaseProcessor().process("hello world")
    ReverseProcessor().process("hello world")
