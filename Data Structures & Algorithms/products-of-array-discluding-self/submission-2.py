class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        pre_multiplier = 1
        for i in range(0, len(nums), 1):
            value = 1
            if i != 0:
                value = nums[i-1] * out[i-1]
            pre_multiplier = pre_multiplier * nums[i]
            out[i] = value

        pos_multiplier = 1
        for i in range(len(nums)-1, -1, -1):
            value = out[-1]
            if i != len(nums)-1:
                value = pos_multiplier * out[i]
            pos_multiplier = pos_multiplier * nums[i]
            out[i] = value
        return out