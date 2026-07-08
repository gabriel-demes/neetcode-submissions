class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights) - 1):
            for t in range(i+1, len(heights)):
                area = (t - i) * min(heights[t], heights[i])
                maxArea = max(maxArea, area)
        
        return maxArea