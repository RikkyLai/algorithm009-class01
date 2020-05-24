/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
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
    ListNode* swapPairs(ListNode* head) {
        // ListNode* pre = new ListNode(0);
        // pre->next = head;
        // ListNode* temp = pre;
        // while (temp->next != NULL && temp->next->next!=NULL) {
        //     ListNode* start = temp->next;
        //     ListNode* end = temp->next->next;
        //     temp->next = end;
        //     start->next = end->next;
        //     end->next = start;
        //     temp = start;
        // }
        // return pre->next;

        // recursive
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode* next = head->next;
        head->next = swapPairs(next->next);
        next->next = head;
        return next;
    }
};
// @lc code=end

