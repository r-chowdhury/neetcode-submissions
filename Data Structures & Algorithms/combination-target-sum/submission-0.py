class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, running_list, running_total):
            if running_total == target:
                res.append(running_list.copy())
                return
            if i >= len(nums) or running_total > target:
                return

            running_list.append(nums[i])
            dfs(i, running_list, running_total + nums[i])
            running_list.pop()
            dfs(i + 1, running_list, running_total)

        dfs(0, [], 0)
        return res
            