#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       j=1
       for i in range(1,len(nums)):
           if(nums[i]!=nums[j-1]):
               nums[j]=nums[i]
               j=j+1
       return j       
               # @lc code=end

