/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
public:
    int trap(vector<int>& height) {
        // int ans = 0;
        // if (height.size() == 0)  return 0;
        // for (int i=0;i<height.size()-1;i++) {
        //     int maxLeft = 0;
        //     int maxRight = 0;
        //     for (int j=i;j>=0;j--) {
        //         maxLeft = max(maxLeft, height[j]);
        //     }
        //     for (int j=i;j<height.size();j++) {
        //         maxRight = max(maxRight, height[j]);
        //     }
        //     ans += min(maxLeft, maxRight) - height[i];
        // }
        // return ans;

        int ans = 0;
        stack<int> stk;
        int current = 0;
        while (current < height.size()) {
            while (!stk.empty() && height[current] > height[stk.top()]){
                int top = stk.top();
                stk.pop();
                if (stk.empty()) break;
                int width = current - stk.top() - 1;
                int bounded_height = min(height[current], height[stk.top()]) - height[top];
                ans += width*bounded_height;
            }
            stk.push(current++);
        }
        return ans;      
    }
};
// @lc code=end

