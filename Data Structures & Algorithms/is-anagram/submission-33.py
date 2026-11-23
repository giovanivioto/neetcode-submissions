class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_table_s = {}
        hash_table_t = {}

        for i, char_s in enumerate(s):
            char_t = t[i]
            hash_table_s[char_s] = hash_table_s.get(char_s, 0) + 1
            hash_table_t[char_t] = hash_table_t.get(char_t, 0) + 1
        
        for char_s in hash_table_s.keys():
            if hash_table_s.get(char_s, 0) != hash_table_t.get(char_s, 0):
                return False
        return True
