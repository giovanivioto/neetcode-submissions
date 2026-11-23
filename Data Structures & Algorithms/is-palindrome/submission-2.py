class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()

        for i in range(0, len(s), 1):
            if s[i] != s[-i-1]:
                return False
        return True