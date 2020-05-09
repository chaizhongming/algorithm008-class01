#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1,cur=[]):
            # print("cur:",cur)
            if len(cur)==k:
                print("cur:",cur)
                print("cur[:]:",cur[:])
                output.append(cur[:])
                output1.append(cur)
                # output.append(cur)
                print("output:",output)
                print("output1:",output1)
                return
            for i in range(first,n+1):
                cur.append(i)
                # print(cur)
                backtrack(i+1,cur)
                cur.pop()
        output=[]
        output1=[]
        backtrack()
        return output1
            
# @lc code=end

