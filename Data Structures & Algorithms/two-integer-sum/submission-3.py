class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Brute Force Solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        

        # trick is to use dict to map index and val & identify diff
        listMap = {}
        for i,n in enumerate(nums):
            diff = target - n # remember this
            if diff in listMap:
                return [listMap[diff],i]
            listMap[n] = i
        return


        