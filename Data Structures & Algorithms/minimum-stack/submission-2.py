class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if self.prefix_stack:
            if self.prefix_stack[0] > val:
                self.prefix_stack.insert(0, val)
            else:
                self.prefix_stack.insert(0, self.prefix_stack[0])
        else:
            self.prefix_stack.insert(0, val)

    def pop(self) -> None:
        self.stack = self.stack[1:]
        self.prefix_stack = self.prefix_stack[1:]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.prefix_stack[0]
