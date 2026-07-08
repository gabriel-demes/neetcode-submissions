class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = nums[i] * -1
            left, right = i + 1, len(nums) - 1

            while left < right: 
                targSum = nums[left] + nums[right]
                if targSum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right + 1] == nums[right] and left < right:
                        right -= 1
                elif targSum > target:
                    right -= 1
                elif targSum < target: 
                    left += 1
        return res