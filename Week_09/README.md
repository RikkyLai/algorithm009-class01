## 学习笔记
### 高级动态规划
#### Review：

```
# terminator
if (level > MAX_LEVEL)
	return 
# process current logic
process(level, param)

# drill down
recur(level:level+1, newParam)
```

分治代码模版

```
def devide_conquer(problem, param1, param2, ...):
	if problem is None:
		print_result
		return
	# prepare data
	data = prepare_data(problem)
	subproblems = split_problem(problem, data)
	# conquer problems
	subresult1 = self.divide_conquer(subproblem[0], p1, ...)
	subresult2 = self.divide_conquer(subproblem[1), p1, ...)
	# process and generate the final resule
	result = process_result(subresult1, subresult2, ...)
```

#### 动态规划

1. “simplifying a complicated problem by breaking it down into simpler sub-problems”
2. Divide & Conquer + Optimal substructure: 分治 + 最优子结构
3. 顺推形式：动态递推  dp[i][j]=_Function(dp[i'][j']...)

复杂来源：1. 状态拥有更多维度     2.状态方程更复杂


### 字符串

```
# 字符串的基本操作：
# 小写字母
str.lower()

# 去除空格并得到list
str.split()

# 对字符串进行计数  (比较常用)
dic = collections.Counter(str)

# 判断字符串元素  是不是数字
str.isalnum()

```

常用的方法： 字典储存、双指针、动态规划的题目


**不同路径2的状态方程**：

if obstacleGrid[i][j] == 0: dp(i,j)=dp(i-1,j)+dp(i,j-1)

if obstacleGrid[i][j] == 1: dp[i][j] = 0



