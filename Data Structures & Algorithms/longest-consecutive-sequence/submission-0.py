class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
        # I want to increase count while i is previous, and j = i+1
        # But I want to traverse the whole list as well 
        