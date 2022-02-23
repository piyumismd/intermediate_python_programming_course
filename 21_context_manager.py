
# open a file then allocate resources and allow changes in the file finally close the file

with open("notes.txt", "w") as file:
    file.write("some ToDo...")

file = open("notes.txt", "w")

try:
    file.write("some ToDo...")
finally:
    file.close()


# class as context manager

class ManagedFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("exit")


with ManagedFile("notes.txt") as file:
    print("do something...")
    file.write("some todo...")
