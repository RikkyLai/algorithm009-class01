# 学习笔记-动态规划

## 字典树和并查集

```
# Python 
class Trie(object):

  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word:
			if char not in node:
				node[char] = {} 
			node = node[char]
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```
例题：单词搜索2

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

输入: 
words = ["oath","pea","eat","rain"] and 

board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]

solve：首先使用字典树存储words里面的单词，然后遍历board，每经历一个board，将搜索它的四连通区域能不能连成一个单词，为了避免重复计算，设置一个标志位。

**使用trie的时间复杂度**：$O(M(4⋅3^{(L−1)}))$，其中M是二维网格中的单元格数，L是单词的最大长度。
最坏情况下该算法循环遍历二维网格中的所有单元，因此在复杂度公式中我们有 M作为因子。然后将其归结为每个启动单元所需的最大步骤数（即 $4\cdot3^{L-1}$）。假设单词的最大长度是 L，从一个单元格开始，最初我们最多可以探索 4 个方向。假设每个方向都是有效的（即最坏情况），在接下来的探索中，我们最多有 3 个相邻的单元（不包括我们来的单元）要探索。这里有一个例子。想象一下，二维网格中的每个单元都包含字母 a，单词词典包含一个单词 ['aaaa']。这是算法将遇到的最坏的情况之一。

## 高级搜索

BFS 模版

```
# Python
def BFS(graph, start, end):
	visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

DFS 模版

```
# 递归模版
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)

# 非递归模版
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...
```

### 双向BFS特性和模版


## 红黑树和AVL树
AVL树：
是一个平衡二叉搜索树
Balance Factor（平衡因子）：{-1, 0, 1}

意思是左子树的高度减去它右子树的高度，高度差只有上面的三个值，将通过旋转操作来进行平衡

红黑树：
近似平衡二叉树，确保任何一个结点的左右子树的高度小于两倍

+ 每个结点要么是红色，要么是黑色
+ 根结点是黑色
+ 每个叶结点是黑色
+ 不能有相邻接的两个红色结点
+ 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点



