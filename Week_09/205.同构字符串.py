#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        hashmap={}
        for i in range(len(s)):
            if s[i] not in hashmap:
                # print(hashmap.values())
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[s[i]]=t[i]
            else:
                if hashmap[s[i]]!=t[i]: 
                    return False
        return True
        
# @lc code=end

