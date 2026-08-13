class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        count = {}
        longest = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFrequency = max(count.values())
            
            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
                maxFrequency = max(count.values())
            longest = max(longest, right - left + 1)

        return longest        