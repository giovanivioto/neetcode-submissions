class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        mono = [[0, 0] for _ in range(len(height))]
        mono[0][0] = height[0]
        mono[len(height) - 1][1] = height[len(height) - 1]
        l, r = 1, len(height) - 2
        while l < len(height) and r >= 0:
            mono[l][0] = max(mono[l-1][0], height[l])
            mono[r][1] = max(mono[r+1][1], height[r])
            l+=1
            r-=1
        for i, h in enumerate(height):
            total += min(mono[i][0], mono[i][1]) - h
        return total