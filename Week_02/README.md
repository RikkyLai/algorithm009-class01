# 学习笔记 
## 哈希表、映射、集合
哈希表 Hash Table，是根据关键码值（Key value）直接进行访问的数据结构，它通过关键码值映射到表中的一个位置来访问记录，以加快查找速度。存放记录的数组叫哈希表，它的查询是 O(1)。但是数组的内存有限，所以有可能根据key映射不同的value，叫哈希碰撞 (Hash Collisions) 所以会想到链表来解决冲突。

```python
# 字母异位组合
class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	dict = {}
	for item in strs:
		key = tuple(sorted(item))
		dict[key] = dict.get(key, []) + [item]
	return list(dict.values())
```



## 树 Tree
关键名词：根 root     父节点  Parent Node    子节点  child node    子树  Sub Tree  

二叉树 Binary Tree：
前序遍历 preorder   中序遍历  inorder   后续遍历  postorder

二叉搜索树 Binary Search Tree：
左子树小于根节点，右子树大于根节点/  一棵空树

方法：递归法  迭代法

```python3
# 树的定义
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self,right = None, None

# 前序、中序、后序递归遍历
def preorder(self, root):
	if root:
		self.traverse_path.append(root.val)
		self.preorder(root.left)
		self.preorder(root.right)

def inorder(self, root):
	if root:
		self.inorder(root.left)
		self.traverse_path.append(root.val)
		self.inorder(root.right)
		
def postorder(self, root):
	if root:
		self.postorder(root.left)
		self.postorder(root.right)
		self.traverse_path.append(root.val)		
```

不过迭代法比较重要，需要用到栈或者队列辅助使用遍历

DFS、BFS （深度优先遍历、广度优先遍历）

BFS: 维护一个队列，保存当前深度的所有节点

DFS：递归

## 堆 Heap 和 二叉堆 Binary Heap
Heap 堆：
可以迅速找到一维数中的最大或者最小值的数据结构

将根节点最大的堆叫做大顶堆或大根堆，根节点最小的堆叫做小顶堆或小根堆。常见有二叉堆、斐波那契堆

二叉堆性质(最小堆)：
1.是一棵完全树          2.树中任意节点的值总是 >= 其节点

二叉堆实现的细节：

1.二叉堆一般通过“数组”实现

2.假设“第一个元素”在数组索引为0，则父节点和子节点位置关系如下：

(1).索引为i的左孩子的索引是 (2i+1)

(2).索引为i的右孩子的索引是 (2i+2)

(3).索引为i的父节点的索引是 floor((i-1)/2)


Insert 插入操作  O(lgN)

1.新元素先插入到尾部     

2.依次向上调整整个堆的结构  （一直到根即可）

Delete Max 删除堆顶操作

1.将堆尾元素替换到顶部  （即堆顶被替代删除）

2.依次从根部向下调整整个堆的结构（一直到堆尾即可）


## 图 Graph
关键名词： Vertex/Vertices 点        Edge 边
图的属性：

1.度  -入度和出度

2.点与点之间是否连通

Adjacency Matrix 邻接矩阵       Adjacency list  邻接表








