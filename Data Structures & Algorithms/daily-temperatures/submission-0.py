class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            y = i - 1
            while y >= 0:
                if temperatures[y] > temperatures[i]:
                    break

                if temperatures[i] > temperatures[y]:
                    if result[y] == 0:
                        result[y] = i - y
                    else:
                        result[y] = min(result[y], i - y)
                y -= 1
        return result