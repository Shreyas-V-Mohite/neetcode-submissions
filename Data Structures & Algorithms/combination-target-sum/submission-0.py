class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            
            # base case if total is equal to target we return it
            if total == target:
                res.append(cur.copy())
                return
            
            # base case if i gets out of bounds | or total is greater than target
            if i >= len(nums) or total > target:
                return

            # main recursion/back tracking logic: a decision tree to skip a number recursively so that repeated permutations of same combinations do not occur.
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0,[],0)

        return res