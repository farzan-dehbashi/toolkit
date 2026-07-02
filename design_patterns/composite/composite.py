class FileSystemItem:
    def __init__(self, name):
        self.name = name

    def get_size(self):
        raise NotImplementedError

    def print_tree(self, indent=0):
        raise NotImplementedError


class File(FileSystemItem):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size

    def print_tree(self, indent=0):
        print(" " * indent + f"📄 {self.name} ({self.size}kb)")


class Directory(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, item):
        self.children.append(item)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def print_tree(self, indent=0):
        print(" " * indent + f"📁 {self.name}/")
        for child in self.children:
            child.print_tree(indent + 2)


if __name__ == "__main__":
    root = Directory("root")
    src = Directory("src")
    src.add(File("main.py", 10))
    src.add(File("utils.py", 5))
    root.add(src)
    root.add(File("README.md", 2))
    root.print_tree()
    print(f"Total size: {root.get_size()}kb")
