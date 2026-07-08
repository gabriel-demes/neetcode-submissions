class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashNums = set(nums)
        for num in nums:
            length = 1
            if num - 1 in hashNums:
                continue 

            while (num + length) in hashNums:
                length += 1
            
            res = max(res, length)

        return res