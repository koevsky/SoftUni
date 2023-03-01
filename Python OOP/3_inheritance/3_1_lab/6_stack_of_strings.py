class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data = self.data + [element]

    def pop(self):
        el = self.data[-1]
        self.data = self.data[:len(self.data)-1]
        return el

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"