class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            prev_list = nums.copy()
            prev_list[i] = 1
            my_expression = "*".join(map(str, prev_list))
            result.append(int(eval(my_expression)))
        return result