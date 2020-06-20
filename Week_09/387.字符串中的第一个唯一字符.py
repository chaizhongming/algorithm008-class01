#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=[i,1]
            else:
                hashmap[s[i]][-1]+=1
        for j in hashmap:
            if hashmap[j][-1]==1:
                return hashmap[j][0]
        return -1


# @lc code=end

