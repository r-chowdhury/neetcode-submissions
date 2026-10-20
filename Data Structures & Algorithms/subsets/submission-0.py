class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, res):
            if i == len(nums):
                ans.append(res.copy())
                return
            num = nums[i]
            res.append(num)
            dfs(i+1, res)
            res.pop()

            dfs(i+1, res)
        dfs(0, []) 
        return ans
