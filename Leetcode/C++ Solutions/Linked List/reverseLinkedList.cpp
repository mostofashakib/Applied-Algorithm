/*
LeetCode Problem: 206. Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = NULL;
        ListNode* temp;
        
        while (curr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};