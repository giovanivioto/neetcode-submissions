class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue

            second = stack.pop()
            first = stack.pop()
            result = int(ops[token](first, second))
            stack.append(result)
        return stack.pop()