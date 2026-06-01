class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        we have to get sum of 2 elements in the list in such a that 
        2 elements are not equal
        - we can use left and right pointers to calculate the sum.
        - decrement right if sum > target and increment left is sum < target
        - repeat this till sum = target
        '''
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[num]=i
        return []







        # l,r=0,len(nums)-1
        # while l < r:
        #     currSum = nums[l]+nums[r]

        #     if currSum < target:
        #         l += 1
        #     elif currSum > target:
        #         r -= 1
        #     else:
        #         return [nums[l],nums[r]]
            # if currSum = target:
            #     for i,n in enumarated(nums):
            #         return [l[i],r[i]]
