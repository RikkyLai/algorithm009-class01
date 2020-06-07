#学习笔记

## 泛型递归、树的递归
树的面试题解法一般是递归:

1. 节点的定义
* 重复性


递归-循环 Recursion： 通过函数体进行的循环

ex：

+ 计算factorial(6)
+ 6*factorial(5)
+ 6\*5*factorial(4)
+ ....

```
# 递归函数模版
def recursion(level, param1, param2):
	# recursion terminator
	if level > MAX_LEVEL:
		process_result
		return
	# 处理当前层
	process(level, param...)
	# drill down
	self.recursion(level+1, p1, ...)
```
就是找最近重复子问题              （ 数学归纳法思维）


## 分治、回溯   （divide & conquer）
寻找问题的重复性，一般都会有

```
# 分治模版
def divide_conquer(problem, param1, param2, ...):
	# recursion terminator
	if problem is None:
		print_result
		return	
	# prepare data
	data = prepare_data(problem)
	# conquer subproblems
	subproblems = split_problem(problem, data)
	subresult1 = self.divide_conquer(subproblem[0], p1, ...)
	subresult2 = self.divide_conquer(subproblem[1], p1, ...)
	...
	# process and generate the final result
	result = process_result(subresult, subresult2, ..)
```

回溯：把所有方法列举一遍








