class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l = 0
        r = 1
        recent = {s[l]: 0}
        longest = 1

        while r < len(s) and l < r:
            if s[r] in recent and recent[s[r]] < l:
                longest = max(longest, r - l + 1) 
                recent[s[r]] = r
                r += 1
            elif s[r] not in recent:
                recent[s[r]] = r
                longest = max(longest, r - l + 1) 
                r += 1
            else:
                l = recent[s[r]] + 1
                recent[s[r]] = r
                r += 1
        return longest

            

        