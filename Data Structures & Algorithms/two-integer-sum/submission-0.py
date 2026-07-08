class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceIndex = {}

        for i in range(len(nums)):
            if nums[i] in differenceIndex:
                return [differenceIndex[nums[i]], i]
            
            differenceIndex[target - nums[i]] = i