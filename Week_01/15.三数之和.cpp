/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        if (nums.size() < 3) return res;
        for (int i=0; i<nums.size()-1;i++) {
            int target = -nums[i];
            int left = i+1;
            int right = nums.size()-1;
            while (left < right) {
                if (target == nums[left] + nums[right]) {
                    vector<int> r(3, 0);
                    r[0] = nums[i];
                    r[1] = nums[left];
                    r[2] = nums[right];
                    res.push_back(r);
                    while(left<right && nums[right]==r[2]) right--;
                    while(left<right && nums[left] == r[1]) left++; 
                }
                else if (nums[left] + nums[right] > target) {
                    
                    right--;
                }
                else {
                    
                    left ++;
                }
                
            }
            while (i<nums.size()-1 && nums[i+1] == nums[i]) i++;
        }
        return res;
    }
};
// @lc code=end

