#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_max=[]
        nums_counts={}
        top_k=[]
        for i in nums:
            nums_counts[i]= nums_counts[i]+1 if i in nums_counts else 1
        for j in nums_counts:
            heapq.heappush(heap_max,(-nums_counts[j],j))
        for l in range(k):
            value=heapq.heappop(heap_max)
            top_k.append(value[1])
        return top_k
# @lc code=end

