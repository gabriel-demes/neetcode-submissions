class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        start = 0
        end = len(lower) - 1
        
        while(start < end):
            if not lower[start].isalnum():
                start += 1
            elif not lower[end].isalnum():
                end -= 1
            elif lower[start] != lower[end]:
                return False
            else:
                start += 1
                end -= 1

        return True
