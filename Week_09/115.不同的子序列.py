#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1=len(t)
        n2=len(s)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for j in range(n2+1):
            dp[0][j]=1
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]
        
# @lc code=end

