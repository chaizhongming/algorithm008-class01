#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0
        dp=[0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i]=="(":
                dp[i]=0
            else:
                if i>=1 and s[i-1]=="(":
                    dp[i]=dp[i-2]+2 if i>=2 else 2
                if s[i-1]==")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2 if i-dp[i-1]-2>=0 else dp[i-1]+2
        return max(dp)
# @lc code=end

