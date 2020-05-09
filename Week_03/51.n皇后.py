#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        def DFS_NQueens(cols,pie,na):
            p=len(cols)
            if p==n:
                result.append(cols)
                return None
            for q in range(n):
                if q not in cols and p+q not in pie and p-q not in na:
                    DFS_NQueens(cols+[q],pie+[p+q],na+[p-q])
        DFS_NQueens([],[],[])
        return [["."*i+"Q"+"."*(n-i-1) for i in sol] for sol in result]
# @lc code=end

