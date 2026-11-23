class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##1,2,3,4....
        ##O(n) time
        ##O(n) space
        my_hash = set(nums)
        sequences = {}
        if not nums:
            return 0
        for i, n in enumerate(nums):
            if n-1 not in my_hash:
                if n not in sequences:
                    sequences[n] = 1

                if sequences[n] > 1:
                    continue

                i=1
                while n+i in my_hash:
                    sequences[n] += 1
                    i+=1

        return max(sequences.values())