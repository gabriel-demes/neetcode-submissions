class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        r = 0
        total = 0

        while r < len(arr):
            total += arr[r]

            if r - l + 1 == k:
                if total >= threshold * k:
                    count += 1
                total -= arr[l]
                l += 1
            r += 1
        
        return count

