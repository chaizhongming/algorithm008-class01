#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            if target-nums[i] in hash_map:
                return [hash_map[target-nums[i]],i]
            else:
                hash_map[nums[i]]=i
# @lc code=end

