class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        right_pointer = len(heights) - 1
        if len(heights) <= 2:
            return min(heights[0], heights[1])

        for left_pointer, left_height in enumerate(heights):
            while right_pointer > left_pointer:
                right_height = heights[right_pointer]
                side_a = right_pointer - left_pointer
                side_b = min(left_height, right_height)
                area = side_a * side_b
                if area >= highest:
                    highest = area
                if left_height >= right_height:
                    right_pointer -= 1
                else:
                    break


        return highest
