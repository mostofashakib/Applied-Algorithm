/*
LeetCode Problem: 92. Reverse Linked List II
Link: https://leetcode.com/problems/reverse-linked-list-ii/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        
        while (left > 1) {
            prev = curr;
            curr = curr->next;
            left--;
            right--;
        }
        
        ListNode* connection = prev;
        ListNode* tail = curr;
        ListNode* temp;
        
        while (right > 0) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
            right--;
        }
        
        if (connection != NULL) {
            connection->next = prev;
        }
        else {
            head = prev;
        }
        
        tail->next = curr;
        
        return head;
    }
};