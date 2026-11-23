class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##1,2,3,4....
        ##O(n) time
        ##O(n) space
        my_hash = set(nums)
        longer = 0
        if not nums:
            return 0
        for n in nums:
            if n-1 not in my_hash:
                lenght = 1
                while n+lenght in my_hash:
                    lenght += 1
                longer = max(lenght, longer)

        return longer