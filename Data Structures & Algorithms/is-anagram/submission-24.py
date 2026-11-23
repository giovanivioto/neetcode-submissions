class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash_s = {}
        my_hash_t = {}
        for x in s:
            my_hash_s[x] = my_hash_s.get(x, 0) + 1

        for i in t:
            if i not in my_hash_s:
                return False
            my_hash_t[i] = my_hash_t.get(i, 0) + 1

        for key, value in my_hash_t.items():
            if value != my_hash_s[key] or key not in my_hash_s:
                return False
            return True