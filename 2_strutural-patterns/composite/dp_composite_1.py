#!/usr/bin/python3

class File():
    def __init__(self, name):
        self.name = name

class Folder(list):
    pass

file1 = File("file1")
file2= File("file2")

folder1 = Folder()
folder2 = Folder()

folder1.append(file1)
folder1.append(folder2)

folder2.append(file2)

# folder1
# |- file1
# |- folder2
#     |- file2

print(folder1)