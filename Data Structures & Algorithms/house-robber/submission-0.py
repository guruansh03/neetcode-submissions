class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 0
        dp = {}
        def robs(nums,i):
            if i  >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            r = nums[i] + robs(nums,i+2)
            nr = 0 + robs(nums,i+1)
            dp[i] = max(r,nr)
            return dp[i]
        x = robs(nums,i)
        return x