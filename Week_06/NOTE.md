本周完成了最小路径和、最长有效括号、最大正方形、青蛙过河4道作业

1）最大正方形：这道题的难点主要的递推方程不容易想道，需要看1277题的详细推导，采用不等式两端夹闭的方式。
f[i][j]=min(f[i][j−1],f[i−1][j],f[i−1][j−1])+1

2）最小路径和：这道题相对来说比较简单一些，典型的动态规划题目。一个技巧是可以不用单独定义dp，直接用grid可以节省空间，另外几个技巧是直接用一个一维数组代替二位数组dp，比较巧妙，主要状态转移方程：
        g[j]=min(g[j-1],g[j])+grid[i][j] 

3）青蛙过河：这道题的难点是正对于每个stone[i]，有几个不同的step状态，要对其进行遍历，开始自己做的时候没想到这个。

4）最长有效括号，这道题是递推方程比较巧妙，自己想的时候没有想到。

dp[i]=dp[i-2]+2

dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2

另外一个就是边界条件，容易出错，数组不要越界。下面一段代码用一个open变量回避了边界问题，很妙。

public int longestValidParentheses(String s) {

    char[] S = s.toCharArray();
    int[] V = new int[S.length];
    int open = 0;
    int max = 0;
    for (int i=0; i<S.length; i++) {
        if (S[i] == '(') open++;
        if (S[i] == ')' && open > 0) {
            // matches found
            V[i] = 2+ V[i-1];
            // add matches from previous
            if(i-V[i]>0)
                V[i] += V[i-V[i]];
            open--;
        }
        if (V[i] > max) max = V[i];
    }
    return max;
}