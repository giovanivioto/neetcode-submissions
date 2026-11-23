class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums) // 2
        result = -1
        count = 0
        while count <= len(nums):
            prev = nums[index]
            if target == prev:
                result=index
                break
            elif target > prev:
                index += len(nums[index:]) // 2
            elif target < prev:
                index = index - len(nums[:index]) // 2 if len(nums[:index]) // 2 != 0 else 0
            count+=1
        return result