class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        pos = [1 for _ in range(len(nums))]
        pre = [1 for _ in range(len(nums))]
        for i in range(0, len(nums), 1):
            register = i-1
            multiplier = 1
            if i != 0:
                multiplier = pre[register]
            pre[i] = multiplier * nums[i]

        for i in range(len(nums)-1, -1, -1):
            register = i+1
            multiplier = 1
            if i != len(nums)-1:
                multiplier = pos[register]
            pos[i] = multiplier * nums[i]

        for i in range(0, len(nums), 1):
            pre_value = 1
            pos_value = 1
            if i != 0:
                pre_value = pre[i-1]
            if i != len(nums)-1:
                pos_value = pos[i+1]
            out[i] = pre_value*pos_value
        return out