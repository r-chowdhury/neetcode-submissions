class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        i = 2
        while i < len(nums):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            i += 1
        return max(dp)