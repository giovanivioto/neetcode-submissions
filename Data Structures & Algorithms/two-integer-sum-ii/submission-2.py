class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left_pointer = 0
        right_pointer = -1
        while not result:
            left_value = numbers[left_pointer]
            right_value = numbers[right_pointer]
            if left_value + right_value > target:
                right_pointer -= 1
            elif left_value + right_value < target:
                left_pointer += 1
            else:
                result = [left_pointer+1, (len(numbers) + right_pointer)+1]
        return result
