#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            j=min(i+k-1,len(s)-1)
            while(i<j):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
# @lc code=end

