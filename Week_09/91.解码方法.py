#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        s=list(s)
        dp=[ 0 for _ in range(len(s))]
        if int(s[0])>0:
            dp[0]=1
        else:
            return 0
        for i in range(1,len(s)):
            if int(s[i-1])==2:
                if int(s[i])>6:
                    dp[i]=dp[i-1]
                elif int(s[i])>=1:
                    dp[i]=dp[i-1]+dp[i-2] if i>=2 else dp[i-1]+1
                else:
                    dp[i]=dp[i-2] if i>=2 else 1
            elif int(s[i-1])==1:
                if int(s[i])>0:
                    dp[i]=dp[i-1]+dp[i-2] if i>=2 else dp[i-1]+1
                else:
                    dp[i]=dp[i-2] if i>=2 else 1
            else:
                if int(s[i])>0:
                    dp[i]=dp[i-1]
                else:
                    return 0

        return dp[-1]
# @lc code=end

