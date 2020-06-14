# 学习笔记

## 深度优先搜索和广度优先搜索(deep first or breadth first)
两种方式只是访问的节点顺序不一样，所以分别存储进入栈或者队列。深度优先是先一条路走到黑再回来从另一个路径继续到尽头；广度优先搜索是先把当前层先遍历再继续下一层。

```
# dfs模版1
def dfs(node):
	if node in visited:
		return
	visited.add(node)
	# process current node
	dfs(node.left)
	dfs(node.right)
	
# dfs模版2
def DFS(self, root):
	if root in None:
		return None
	visited, stack = [], [root]
	while stack:
		node = stack.pop()
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)
```

```
# bfs模版
def bfs(graph, start, end):
	queue = []
	queue.append([start])
	visited.add(start)
	while queue:
		node = queue.pop()
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
		queue.push(nodes)
```

## 贪心算法
每一步选择中选取当前状态下最好或最优，即希望能够导致全局最好或最优的算法

与动态规划不同: 对于每个子问题的解决方案都做出选择，动态规划则会保存以前的运算结果


## 二分查找
前提：

+ 目标函数单调性
+ 存在上下界
+ 能够通过索引访问

代码模版

```
left, right = 0, len(array)-1
while left <= right:
	mid = left + (right - left)//2
	if array[mid] == target:
		# find the target
		break or return result
	elif array[mid] < target:
		left = mid + 1
	else:
		right = mid - 1  
```

思考题：寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

思路：

1. 暴力破解，从第一个开始循环，找到 array[k] < array[k-1] 或者 不再有单调的地方
2. 二分查找，找到中间点，看是否单调，即array[mid] > array[left], 如果是，那么无序的地方就在右边，left = mid + 1；如果不是，无序的地方在左边，right = mid -1 


