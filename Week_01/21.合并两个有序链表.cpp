/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* pre=new ListNode(-1);
        ListNode* temp = pre;
        while (l1!=NULL && l2!=NULL) {
            if (l1->val <= l2->val) {
                temp->next = l1;
                temp = l1;
                l1 = l1->next;
            }
            else {
                temp->next = l2;
                temp = l2;
                l2 = l2->next;
            }
        }
        temp->next = l1==NULL?l2:l1;
        return pre->next;
    }
};
// @lc code=end

