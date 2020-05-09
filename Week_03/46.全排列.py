#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first==n:
                res.append(nums[:])
            for i in range(first,n):
                nums[i],nums[first]=nums[first],nums[i]
                backtrack(first+1)
                nums[first],nums[i]=nums[i],nums[first]
        n=len(nums)
        res=[]
        backtrack()
        return res
# @lc code=end

