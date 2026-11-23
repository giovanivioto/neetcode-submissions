class Solution:
    def isValid(self, s: str) -> bool:
        register = []
        index = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for c in s:
            if c in index:
                if not register or register.pop() != index[c]:
                    return False
            else:
                register.append(c)
        return not register