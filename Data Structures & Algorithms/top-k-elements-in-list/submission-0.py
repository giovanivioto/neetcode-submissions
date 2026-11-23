class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##so posso fazer uma iteração no elemento nums
        ##k é o top elementos que aparecem
        hash = {}
        buckets = []
        for num in nums:
            frequency = nums.count(num)
            if num not in hash:
                hash[num] = frequency
            buckets.append([])

        for num, frequency in hash.items():
            buckets[frequency-1].append(num)

        result = []
        rounds = 0
        while len(result) < k:
            if buckets[-1-rounds]:
                result.extend(buckets[-1-rounds])
            rounds += 1

        return result