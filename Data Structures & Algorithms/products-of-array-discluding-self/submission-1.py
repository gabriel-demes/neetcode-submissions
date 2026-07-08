class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prodArray = []
        countZero = 0
        for num in nums:
            if num == 0:
                countZero += 1
            else: 
                product *= num  
        
        for num in nums:
            if countZero > 1:
                prodArray.append(0)
            elif countZero > 0 and num != 0:
                prodArray.append(0)
            elif num == 0:
                prodArray.append(product)
            else:
                prodArray.append(product//num)
            
        
        return prodArray
