class MinStack:
    def __init__(self):
        self._stack = []
        self._lowest = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append(val)
            self._lowest.append(0)
            return

        self._stack.append(val)

        if val == self._stack[self._lowest[-1]] or val < self._stack[self._lowest[-1]]:
            self._lowest.append(len(self._stack) - 1)
            return
        else:
            i = -1
            while val > self._stack[self._lowest[i]]:
                if i == -len(self._lowest):
                    break
                i-=1

        self._lowest.insert(0, len(self._stack) - 1)
        return

    def getMin(self) -> int:
        return self._stack[self._lowest[-1]]

    def pop(self) -> None:
        if self._lowest[-1] == len(self._stack) - 1:
            self._lowest.pop()
            self._stack.pop()
            return

        self._lowest.remove(len(self._stack) - 1)
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]