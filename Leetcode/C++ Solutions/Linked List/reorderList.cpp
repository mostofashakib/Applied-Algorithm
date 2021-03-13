/*
LeetCode Problem: 143. Reorder List
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL) {
            return;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while ( fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        ListNode* prevNode = NULL;
        ListNode* nextNode;
        
        while (slow != NULL) {
            nextNode = slow->next;
            slow->next = prevNode;
            prevNode = slow;
            slow = nextNode;
        }
        
        ListNode* first = head;
        ListNode* second = prevNode;
        ListNode* temp;
        
        while (second->next != NULL) {
            temp = first->next;
            first->next = second;
            first = temp;
            
            temp = second->next;
            second->next = first;
            second = temp;
        }
    }
};