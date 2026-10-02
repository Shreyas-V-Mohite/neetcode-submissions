class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #brute force sol
        # res = defauldict(list)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())
        
        # now for optimal solution: look at the frequence of the chars in the word can we map it? use the ord to look at ascii val so cal can be done
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # we keep this inside to reset after every iter
            for c in s:
                count[ord(c) - ord('a')] += 1 
            res[tuple(count)].append(s) # here tuple is important as they are hashable and lists are not.
        return list(res.values())

