class Solution:

    def encode(self, strs: List[str]) -> str:
        # sizeS = []
        # if len(str) = 0:
        #     return emptystring

        # for s in strs :
        #     len(s).append(sizeS)
        #     encodedS = (countS + "#")
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        
        return res



    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : length + j + 1]) # j + 1 = #
            i = length + j + 1
        return res
