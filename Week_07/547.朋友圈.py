#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class UnionFind(object):
    def __init__(self,n):
        self.p=[i for i in range(n)]
    def union(self,i,j):
        p1=self.parent(i)
        p2=self.parent(j)
        self.p[p1]=p2
    def parent(self,i):
        while self.p[i]!=i:
            self.p[i]=self.p[self.p[i]]
            i=self.p[i]
        return i
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n=len(M)
        uf=UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    uf.union(i,j)
        return len(set(uf.parent(i) for i in range(n)))        
# @lc code=end
