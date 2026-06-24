class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        def robs(nums,i,dp):
            if i  >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            r = nums[i] + robs(nums,i+2,dp)
            nr = 0 + robs(nums,i+1,dp)
            dp[i] = max(r,nr)
            return dp[i]
        x = robs(nums[1:],i,{})
        y = robs(nums[0:n-1],i,{})
        return max(x,y)