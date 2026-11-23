class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        my_hash = {}
        for i, item in enumerate(strs):
            s = "".join(sorted(item))
            if s not in my_hash:
                my_hash[s] = []
            my_hash[s].append(i)

        for _, sorted_list in my_hash.items():
            prev = []
            for index in sorted_list:
                prev.append(strs[index])
            result.append(prev)
        return result