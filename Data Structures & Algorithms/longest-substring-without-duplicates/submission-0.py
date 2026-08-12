class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longestString = 0
        seen = set()
        left, right = 0, 0
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                longestString = max(longestString, right - left)
            else:
                seen.remove(s[left])
                left += 1
            
        return longestString

