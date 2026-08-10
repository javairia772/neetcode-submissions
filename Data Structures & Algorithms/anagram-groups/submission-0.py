class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for str in strs:
            sorted_word = "".join(sorted(str))
            anagramList[sorted_word].append(str)                
        return list(anagramList.values())
