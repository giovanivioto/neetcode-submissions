class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        i=0
        while i < (len(nums) - 1):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue

            left_pointer = i+1
            right_pointer = len(nums)-1
            target = nums[i] * -1
            while left_pointer < right_pointer:
                left_value = nums[left_pointer]
                right_value = nums[right_pointer]
                sum = left_value + right_value
                if sum < target:
                    left_pointer += 1
                elif sum > target:
                    right_pointer -= 1
                else:
                    triplets.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while [left_pointer] == nums[left_pointer-1]:
                        if left_pointer > len(nums)-1:
                            break
                        left_pointer += 1

                    while nums[right_pointer] == nums[right_pointer+1]:
                        if right_pointer <= 0:
                            break
                        right_pointer -= 1
            i+=1
        return triplets