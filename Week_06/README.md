# 学习笔记-动态规划

分治法模版

```
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

递归模版

```
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```


## Dynamic Programming
Define：Simplifying a complicated problem by breaking it down into simpler sub-problems

和递归、分治没有根本区别，共性就是找到重复子问题，差异性是最优子结构、中途可以淘汰次优解

关键点：

+ 最优子结构
```   
 	opt[n] = best_of(opt[n-1], opt[n-2], ...)
```

+ 存储中间状态
```
opt[i]
```

+ 递推公式（状态转移方程或DP方程）

```
Fib: opt[n]=opt[n-1] + opt[n-2]
二维路径：opt[i][j] = opt[i+1] + opt[i][j+1]
```

### easy steps to DP

1. define subproblems
2. guess(part of solution)
3. relate subproblem solutions 
4. recurse of memories / build DP table
5. solve original problems

## 股票问题
分析问题的各种状态，股票问题最基本有三个状态：天数、交易次数、持股（1/0），所以根据状态，股票问题可以列出一个三维矩阵，dp[i][j][k]表示当前的状态：第i天交易次数为j持股状态为k。动态规划问题通常就是状态转移的过程，当前状态与之前的状态有关

1.交易次数为 1:

```
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
            = max(dp[i-1][1][1], -prices[i])
解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。

现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。
可以进行进一步化简去掉所有 k：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])

```
2.交易次数为常数

```
int max_k = 2;
int[][][] dp = new int[n][max_k + 1][2];
for (int i = 0; i < n; i++) {
    for (int k = max_k; k >= 1; k--) {
        if (i - 1 == -1) { 
            /* 处理 base case */
            dp[i][k][0] = 0;
            dp[i][k][1] = -prices[i];
            continue;
        }
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
    }
}
// 穷举了 n × max_k × 2 个状态，正确。
return dp[n - 1][max_k][0];
```

3.有手续费，不限交易次数

```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
```

4.有交易冷冻期，不限交易次数

```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
```

## 斐波拉契数列
爬楼梯，一维数据的状态转移，Fib: opt[n]=opt[n-1] + opt[n-2]

```
	first = 1
	second = 1
	if n == 0 or n==1:
	    return n
	third = 0
	for i in range(2, n+1):
	    third = first + second
	    first = second
	    second = third
	return third
```

编码方式问题：

1.定义状态

既然结尾的字符很重要，在定义状态的时候可以这样定义：

dp[i]：以 s[i] 结尾的前缀子串有多少种解码方法。

2.推导状态转移方程

如果 s[i] == '0' ，字符 s[i] 就不能单独解码，所以当 s[i] != '0' 时，dp[i] = dp[i - 1] * 1。
说明：为了得到长度为 i + 1 的前缀子串的解码个数，需要先得到长度为 i 的解码个数，再对 s[i] 单独解码，这里分了两步，根据「分步计数原理」，用乘法。这里的 1 表示乘法单位，语义上表示 s[i] 只有 1 种编码。

如果当前字符和它前一个字符，能够解码，即 10 <= int(s[i - 1..i]) <= 26，即 dp[i] += dp[i - 2] * 1；
说明：不同的解码方法，使用「加法」，理论依据是「分类计数的加法原理」，所以这里用 +=。

注意：状态转移方程里出现了下标 i - 2，需要单独处理（如何单独处理，需要耐心调试）。

3.初始化

如果首字符为 0 ，一定解码不了，可以直接返回 0，非零情况下，dp[0] = 1；

4.考虑输出

输出是 dp[len - 1]，符合原始问题。

5.考虑优化空间

这里当前状态值与前面两个状态有关，因此可以使用三个变量滚动计算。但空间资源一般来说不紧张，不是优化的方向，故不考虑。


```
	m = len(s)
	if(not s or s[0]=="0"):
	    return 0     
	dp = [0] * (m+1)
	dp[0] = 1
	dp[1] = 1
	for i in range(1, m):
	    if s[i] == "0":
	        if s[i-1] == '1' or s[i-1] == '2':
	            dp[i+1] = dp[i-1]
	        else:
	            return 0
	    elif s[i-1] == '1' or s[i-1] == '2' and '1'<=s[i]<='6':
	        dp[i+1] = dp[i] + dp[i-1]
	    else:
	        dp[i+1] = dp[i]
	
	return dp[-1]
```

### 编辑距离 DP二维表
+ 在单词 A 中插入一个字符：如果我们知道 horse 到 ro 的编辑距离为 a，那么显然 horse 到 ros 的编辑距离不会超过 a + 1。这是因为我们可以在 a 次操作后将 horse 和 ro 变为相同的字符串，只需要额外的 1 次操作，在单词 A 的末尾添加字符 s，就能在 a + 1 次操作后将 horse 和 ro 变为相同的字符串；

+ 在单词 B 中插入一个字符：如果我们知道 hors 到 ros 的编辑距离为 b，那么显然 horse 到 ros 的编辑距离不会超过 b + 1，原因同上；

+ 修改单词 A 的一个字符：如果我们知道 hors 到 ro 的编辑距离为 c，那么显然 horse 到 ros 的编辑距离不会超过 c + 1，原因同上。


```
	m = len(word1) + 1
	n = len(word2) + 1
	dp = [[0]*n for _ in range(m)]
	for i in range(n):
	    dp[0][i] = i
	for j in range(m):
	    dp[j][0] = j
	for i in range(1, m):
	    for j in range(1, n):
	        if word1[i - 1] == word2[j - 1]:  
	            dp[i][j] = dp[i - 1][j - 1]
	        else:   # 删除、插入、替换
	            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
	return dp[-1][-1]
```