class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for index_str in range(0, len(strs), 1):
            my_key = [0]*26
            for index_str_1 in range(0, len(strs[index_str]), 1):
                my_key[ord(strs[index_str][index_str_1]) - ord('a')] += 1
            if tuple(my_key) not in hash:
                hash[tuple(my_key)] = []
            hash[tuple(my_key)].append(strs[index_str])
        return list(hash.values())