class MinStack:
    def __init__(self):
        self._stack = []
        self._lowest = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append(val)
            self._lowest.append(val)
            return

        self._stack.append(val)
        self._lowest.append(min(val, self._lowest[-1]))
        return

    def getMin(self) -> int:
        return self._lowest[-1]

    def pop(self) -> None:
        self._lowest.pop()
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]