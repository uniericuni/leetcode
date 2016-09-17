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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        
        ListNode *newHead = new ListNode(NULL);
        newHead->next = head;
        ListNode *lNode = newHead;
        
        for(int i=1; i<m; i++)
            lNode = lNode->next;
            
        ListNode *sNode = lNode->next;
        ListNode *node = new ListNode(NULL);
        for(int i=m; i<n; i++){
            node = sNode->next;
            sNode->next = node->next;
            node->next = lNode->next;
            lNode->next = node;
        }
        
        if(m==1)
            return lNode->next;
        else
            return head;
            
    }
};
