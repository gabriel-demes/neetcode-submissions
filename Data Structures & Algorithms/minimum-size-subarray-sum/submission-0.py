class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minarr = 0
        total = nums[l]

        while r < len(nums):
            if total >= target:
                if r - l + 1 < minarr or minarr == 0:
                    minarr = r - l + 1
                
                total -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    total += nums[r]
        return minarr
                