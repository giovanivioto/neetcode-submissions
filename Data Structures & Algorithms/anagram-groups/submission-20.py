class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            s_sorted = "".join(list(sorted(s)))
            if s_sorted not in hash_map:
                hash_map[s_sorted] = []
            hash_map[s_sorted].append(s)
        return list(hash_map.values())