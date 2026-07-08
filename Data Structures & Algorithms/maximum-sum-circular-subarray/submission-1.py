class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        gMax, gMin = nums[0], nums[0]
        total = 0

        for num in nums:
            total += num
            curMax = max(num, curMax + num)
            curMin = min(curMin + num, num) 
            gMax = max(curMax, gMax)
            gMin = min(curMin, gMin)
        
        return max(total - gMin, gMax) if gMax > 0 else gMax
