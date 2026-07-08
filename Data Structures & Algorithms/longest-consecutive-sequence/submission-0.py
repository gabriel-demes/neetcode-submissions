class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashNums = set(nums)
        for num in nums:
            start = num
            length = 1
            if num - 1 in hashNums:
                continue 

            while (start + 1) in hashNums:
                start += 1
                length += 1
            
            res = max(res, length)

        return res