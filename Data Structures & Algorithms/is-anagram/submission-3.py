class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash_s = {}
        my_hash_t = {}
        for i in range(len(s)):
            if s[i] not in my_hash_s:
                my_hash_s[s[i]] = 0
            my_hash_s[s[i]] += 1

            if t[i] not in my_hash_t:
                my_hash_t[t[i]] = 0
            my_hash_t[t[i]] += 1
        
        for string_s, count_s in my_hash_s.items():
            if string_s not in my_hash_t:
                return False
            if count_s != my_hash_t[string_s]:
                return False
        return True