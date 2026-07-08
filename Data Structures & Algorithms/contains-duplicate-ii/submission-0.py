class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       indx = {}

       for i in range(len(nums)):
            if nums[i] in indx and i - indx[nums[i]] <= k:
                return True
            else :
                indx[nums[i]] = i

       return False
