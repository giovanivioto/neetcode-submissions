class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        right_pointer = len(heights) - 1
        if len(heights) <= 2:
            return min(heights[0], heights[1])

        for left_pointer, left_height in enumerate(heights):
            while right_pointer > left_pointer:
                area = (right_pointer - left_pointer) * min(left_height, heights[right_pointer])
                highest = max(highest, area)
                if left_height >= heights[right_pointer]:
                    right_pointer -= 1
                else:
                    break
        return highest