class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##minimo dois elementos em nums
        ##numeros dentro de nums podem ser negativos
        ##target tambem pode ser negativo
        my_hash = {}

        for i, num in enumerate(nums):
            if target - num in my_hash:
                return [my_hash[target - num], i]
            my_hash[num] = i