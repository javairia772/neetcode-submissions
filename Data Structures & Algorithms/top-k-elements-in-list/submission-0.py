class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]   
        

        