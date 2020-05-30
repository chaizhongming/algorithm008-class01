#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        steps=defaultdict(set)
        steps[stones[0]].add(0)
        for i in range(len(stones)):
            for step in steps[stones[i]]:
                for k in range(step-1,step+2):
                    if k>0 and stones[i]+k in stones:
                        steps[stones[i]+k].add(k) 
        return len(steps[stones[-1]])>0      
# @lc code=end

