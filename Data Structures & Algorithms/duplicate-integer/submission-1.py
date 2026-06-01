class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False
'''
we want to check if there are repeated nos in the list.
One way to do this is to compare the length of list 
with length of set of list.
'''