from pathlib import Path
# print(Path.home().cwd)
# path = Path.home()
# print(path.is_dir())
# print(path.is_file())
# print(path.exists())
# print(path.name)
# print(path.suffix)
# print(path.stem)
# print(path.parent)
# print(path.anchor)
# print(path.drive)
# print(path.parts)
# print(path.root + "root")
# print(path.stat() + "stat")
# print(path.lstat() + "lstat")

# print([*Path("./").iterdir()])
# print(type(Path("./").iterdir()))
path = Path("./")
print([p for p in path.iterdir() if p.is_dir()])