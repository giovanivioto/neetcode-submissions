class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##minimo dois elementos em nums
        ##numeros dentro de nums podem ser negativos
        ##target tambem pode ser negativo
        my_hash = {}

        for index_num in range(0, len(nums) - 1, 1):
            for index_num_1 in range(index_num + 1, len(nums), 1):
                if nums[index_num] + nums[index_num_1] == target: 
                    if nums[index_num] + nums[index_num_1] not in my_hash:
                        my_hash[nums[index_num] + nums[index_num_1]] = []
                    my_hash[nums[index_num] + nums[index_num_1]].append([index_num,index_num_1])
        return my_hash[target][0]