class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

stack = Stack()

print("Pushing 4 elements: 35,25,91,16")
stack.push(35)
stack.push(25)
stack.push(91)
stack.push(16)
print("Popping 2 elements:")
print(stack.pop())
print(stack.pop())