class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash_s = {}
        my_hash_t = {}
        for i in range(len(s)):
            my_hash_s[s[i]] = my_hash_s.get(s[i], 0) + 1
            my_hash_t[t[i]] = my_hash_t.get(t[i], 0) + 1

        for key, value in my_hash_t.items():
            if value != my_hash_s.get(key, 0) or key not in my_hash_s:
                return False
        return True