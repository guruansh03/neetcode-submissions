class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def paths(m,n):
            if m == 1 or n == 1:
                return 1
            if (m,n) in dp:
                return dp[m,n]
            else:
                dp[m,n]=paths(m-1,n) + paths(m,n-1)
            return dp[m,n]
        x = paths(m,n)
        return x
       