class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                    longest = max(length,longest)
        return longest
        ''' here I started with n-1 not in set
but did not consider the longest and length var which
was the actual requirement of the solution.
'''
