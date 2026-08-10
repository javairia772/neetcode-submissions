class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        for i in range (len(s)):
            char = s[i]
            if char in s_dic:
                s_dic[char] += 1
            else:
                s_dic[char] = 1
        
        for j in range (len(t)):
            char = t[j]
            if char in s_dic:
                s_dic[char] -= 1

        for char in s_dic:
            if s_dic[char] != 0:
                return False
        return True
        
        
            