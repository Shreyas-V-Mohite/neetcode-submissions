class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs,ct = {},{}
        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i],0)
            ct[t[i]] = 1 + ct.get(t[i],0)
            '''
            we assign the count of the same char in the str to 
            the key in the dict(hash map)
            '''
        for c in cs:
            if cs[c] != ct.get(c,0):
                return False
            '''
            then compare this count
            with the other dict.
            '''
        return True