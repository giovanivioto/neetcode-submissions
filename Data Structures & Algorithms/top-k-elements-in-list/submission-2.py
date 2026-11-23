class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##so posso fazer uma iteração no elemento nums
        ##k é o top elementos que aparecem
        hash = {}
        buckets = [[]]
        for num in nums:
            if num not in hash:
                hash[num] = 0
            hash[num] +=1
            buckets.append([])

        for num, frequency in hash.items():
            buckets[frequency].append(num)

        result = []
        rounds = 0
        while len(result) < k:
            if buckets[-rounds]:
                result.extend(buckets[-rounds])
            rounds += 1

        return result