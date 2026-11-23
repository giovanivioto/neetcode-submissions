class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}

        for i, n in enumerate(nums):
            if (target-n) in my_hash:
                return [my_hash[target-n], i]
            my_hash[n] = i
        return []