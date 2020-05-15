#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_r=len(grid)
        if n_r==0:
            return 0
        n_c=len(grid[0])
        num_islands=0
        for i in range(n_r):
            for j in range(n_c):
                if grid[i][j]=="1":
                    num_islands+=1
                    grid[i][j]="0"
                    queue=collections.deque([(i,j)])
                    while queue:
                        r,c=queue.popleft()
                        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                            if 0<=x<n_r and 0<=y<n_c and grid[x][y]=="1":
                                queue.append((x,y))
                                grid[x][y]="0"
        return num_islands
# @lc code=end

