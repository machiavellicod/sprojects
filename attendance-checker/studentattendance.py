from datetime import datetime


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


stack = Stack()

classOver = False

while not classOver:
    sysProcess = input(
        "Choose an option: \n (1) Add a student \n (2) Remove a student \n (3) Current top student \n (4) Number of student present \n (5) Reverse \n (6) Exit \n Option: "
    )

    if sysProcess == "1":
        studentName = input("Enter Student Name: ")
        currentTime = datetime.now().strftime("%I:%M:%S:%P")
        stpresent = {"timestamp": currentTime, "student": studentName}
        stack.push(stpresent)
        print("Student added")

    if sysProcess == "2":
        if stack.is_empty():
            print("No student to remove")
        else:
            stack.pop()
            print("Student removed from the list")

    if sysProcess == "3":
        if stack.is_empty():
            print("empty")
        else:
            currentTop = stack.peek()
            print(currentTop)

    if sysProcess == "4":
        numOfstudents = stack.size()
        print(numOfstudents)

    if sysProcess == "5":
        for students in reversed(stack.items):
            print(students)

    if sysProcess == "6":
        classOver = True
