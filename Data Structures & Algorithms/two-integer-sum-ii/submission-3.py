class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left_pointer = 0
        right_pointer = -1
        while not result:
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            else:
                result = [left_pointer+1, (len(numbers) + right_pointer)+1]
        return result
