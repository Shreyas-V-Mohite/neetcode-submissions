class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        #chars = a-z
        for s in strs:
            count = [0]*26 #a-z
            for c in s:
                count[ord(c)-ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())