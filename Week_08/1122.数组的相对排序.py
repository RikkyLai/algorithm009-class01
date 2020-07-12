#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = [n for n in arr1 if n not in arr2]
        diff.sort()
        dic = collections.Counter(arr1)
        ans = []
        for i in arr2:
            ans += [i]*dic[i]
        return ans+diff
        
# @lc code=end

