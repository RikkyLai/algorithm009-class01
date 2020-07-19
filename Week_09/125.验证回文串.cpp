/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(string s) {

        int f = 0;
        int e = s.length()-1;
        while (f < e) {
            if (!isalnum(s[f])) {
                f++;
            }
            else if (!isalnum(s[e])) {
                e--;
            }
            else {
                 if (tolower(s[f++]) != tolower(s[e--])) {
                     return false;
                 }
                
            }
        }
        
        
        return true;
    }


};
// @lc code=end

