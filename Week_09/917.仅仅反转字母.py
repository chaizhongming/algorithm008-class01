#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s=list(S)
        i,j=0,len(s)-1
        while i<j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            else:
                if s[i].isalpha()==False:
                    i+=1
                if s[j].isalpha()==False:
                    j-=1
        return "".join(s)

# @lc code=end

