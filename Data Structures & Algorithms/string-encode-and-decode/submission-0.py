class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for s in strs:
            encodeString += f'{len(s)}#{s}' 
        return encodeString

    def decode(self, s: str) -> List[str]:
        decodeList = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            lengthOfWord = int(s[i:j])
            start, end = j+1, j+1+lengthOfWord
            word = s[start : end]
            decodeList.append(word)
            i = end
        return decodeList