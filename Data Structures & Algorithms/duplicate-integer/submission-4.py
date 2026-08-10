class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)):
                if num == nums[j]:
                    count+=1;
                    if(count > 1):
                        flag = True
            count = 0

        if flag:
            return True
        else:
            return False




    



         
         