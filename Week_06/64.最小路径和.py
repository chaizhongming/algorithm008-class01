#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,column=len(grid),len(grid[0])
        for i in range(row):
            for j in range(column):
                if i==0 and j!=0:
                    grid[i][j]=grid[i][j-1]+grid[i][j]
                if i!=0 and j==0:
                    grid[i][j]=grid[i-1][j]+grid[i][j]
                if i!=0 and j!=0:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[row-1][column-1]
# @lc code=end

