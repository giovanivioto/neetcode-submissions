class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [[] for _ in range(len(nums))]
        hash = {}
        for _, num in enumerate(nums):
            hash[num] = hash.get(num, 0) + 1

        for num, count in hash.items():
            result[count-1].append(num)

        final = []
        i = len(nums) - 1
        while len(final) < k:
            if result[i]:
                final.extend(result[i])
            i-=1
        return final