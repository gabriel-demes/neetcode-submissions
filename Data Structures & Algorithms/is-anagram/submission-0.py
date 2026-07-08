class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        letterCount = {}

        for letter in s:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        
        for letter in t:
            if letter not in letterCount:
                return False
            
            letterCount[letter] -= 1
            if letterCount[letter] < 0:
                return False
                
        return True
