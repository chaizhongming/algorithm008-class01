#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def isvalid(self,board,r,c,char):
        for i in range(9):
            if board[r][i]==char or board[i][c]==char or \
            board[3*int(r/3)+int(i/3)][3*int(c/3)+i%3]==char:
                return False
        return True
    def backtrack(self,board):
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.':
                    for char in ["1","2","3","4","5","6","7","8","9"]:
                        if self.isvalid(board,i,j,char):
                            board[i][j]=char
                            if self.backtrack(board):
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board==None or len(board)==0:
            return False
        self.backtrack(board)
    
# @lc code=end

