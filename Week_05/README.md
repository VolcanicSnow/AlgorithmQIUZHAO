**学习笔记**

**爬楼梯扩展**

假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？显示左右可能的路径。

**注意：**给定 *n* 是一个正整数。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        steps = [1, 2]
        self.dfs(n, [], steps)

    def dfs(self, n, res, steps):
        # terminator
        if n == 0:
            print(res)
            return
        for step in steps:
            if n >= step:
                self.dfs(n - step, res + [step], steps)

```

**如果再加一个条件，相邻两步不能走一样的阶数，那么又有几种爬法，显示所有可能的路径**：

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        steps = [1, 2]
        self.dfs(n, [], steps, 0)

    def dfs(self, n, res, steps, prev): # prev 表示上一步所采取的走法
        # terminator
        if n == 0:
            print(res)
            return
        for step in steps:
            if n >= step and step != prev:
                self.dfs(n - step, res + [step], steps, step)
```

**动态规划解法**

```python
# 相邻两步不能一样，该代码只能统计路径总数。
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        if n <= 2: return 2
        k = 3
        dp = [[0] * k for _ in range(n + 1)]
        print(dp)
        # dp[n][k] 表示上到第 n 阶台阶，最后的一步步长是 k
        dp[1][1] = 1
        dp[1][2] = 0
        dp[2][1] = 0
        dp[2][2] = 1
        for i in range(3, n + 1):
            dp[i][1] = dp[i - 1][2]
            dp[i][2] = dp[i - 2][1]

        return sum(dp[n])
```

