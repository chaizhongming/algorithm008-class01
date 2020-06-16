#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum=0
        while(n!=0):
            sum+=1
            n&=n-1
        return sum       
# @lc code=end

