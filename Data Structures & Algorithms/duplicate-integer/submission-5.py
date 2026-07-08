class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = {}
        for x in nums:
            if x in seenNums:
                return True;
            seenNums[x] = 1
        return False
        