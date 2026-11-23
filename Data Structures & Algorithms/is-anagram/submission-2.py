class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash_s = {}
        for x in s:
            if x not in my_hash_s:
                my_hash_s[x] = 0
            my_hash_s[x] += 1

        my_hash_t = {}
        for z in t:
            if z not in my_hash_t:
                my_hash_t[z] = 0
            my_hash_t[z] += 1
        
        for string_s, count_s in my_hash_s.items():
            if string_s not in my_hash_t:
                return False
            if count_s != my_hash_t[string_s]:
                return False
        return True