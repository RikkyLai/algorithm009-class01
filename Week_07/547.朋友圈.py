#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # union set
        parent = [i for i in range(len(M))]
        def find(a):
            root = a
            while parent[root] != root:
                root = parent[root]
            while parent[a] != a:
                temp = a
                a = parent[a]
                parent[temp] = root
            return root
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            parent[p1] = p2

        for a in range(len(M)):
            for b in range(a):
                if M[a][b]:
                    union(a,b)
        for i in range(len(M)): find(i)
        return len(set(parent))

        
        
        # if not M:
        #     return 0
        # n = len(M)
        # res = 0
        # visited = set()
        # def dfs(i):
        #     for j in range(n):
        #         if M[i][j] == 1 and j not in visited:
        #             visited.add(j)
        #             dfs(j)
        # for i in range(n):
        #     if i not in visited:
        #         res += 1
        #         dfs(i)
        # return res


        
# @lc code=end

