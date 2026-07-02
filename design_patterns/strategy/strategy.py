class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy(data)


def bubble(data):
    arr = list(data)
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def python_sort(data):
    return sorted(data)


if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6]

    sorter = Sorter(bubble)
    print(sorter.sort(data))

    sorter = Sorter(python_sort)
    print(sorter.sort(data))
