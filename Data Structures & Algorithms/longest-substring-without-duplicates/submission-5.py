class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_pointer = 0
        last_seen = {}
        longest = 0

        for right_pointer, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left_pointer:
                left_pointer = last_seen[char] + 1
                last_seen.pop(char)
            last_seen[char] = right_pointer
            longest = max(longest, (right_pointer - left_pointer + 1))
        return longest