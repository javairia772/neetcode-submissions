class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)
        leftMul, rightMul = 1, 1

        for i in range(len(nums)):
            res[i] = leftMul
            leftMul *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rightMul
            rightMul *= nums[i]

        return res


        
        