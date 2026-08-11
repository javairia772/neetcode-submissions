class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        longestSequence = 1
        nums = sorted(nums)

        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                continue
            elif(nums[i]+1 == nums[i+1]):
                count += 1 
            else:
                count = 1

            longestSequence = max(count, longestSequence)
        return longestSequence