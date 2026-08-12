class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        maxWater = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = width * height
            maxWater = max(maxWater, area)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return maxWater