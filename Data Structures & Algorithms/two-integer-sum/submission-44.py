class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            search = target - num
            prev = hash_map.get(search, 0)
            if i!=prev and num + nums[prev] == target:
                return [i, prev]