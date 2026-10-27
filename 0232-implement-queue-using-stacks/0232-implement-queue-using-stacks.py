class MyQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def _shift(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        self._shift()
        return self.outbox.pop()

    def peek(self) -> int:
        self._shift()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox
