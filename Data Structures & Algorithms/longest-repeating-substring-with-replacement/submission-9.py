class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        l=0
        r= 0
        charset = {}
        longest = 0
        
        while r < len(s):
            charset[s[r]] = charset.get(s[r], 0) + 1
            
            if (r - l + 1) - max(charset.values()) <= k:
                longest = max(longest, r - l + 1)
                r += 1
            else:
                charset[s[r]] -= 1
                charset[s[l]] -= 1
                if charset[s[l]] == 0: del charset[s[l]]
                l += 1

        return longest