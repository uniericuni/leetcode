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
    ListNode* reverseKGroup(ListNode *head, int k) {
        
        int n=0;
        ListNode *node, *rtn, *p, *preHead, *prev, *listHead;
        
        node=head; rtn=head;
        
        while(node){
            n++;
            node = node->next;
        }
        
        bool headFlag = false;
        int r = n%k, q = n/k;
        
        preHead = p;
        node = head;
        listHead = preHead;
        for(int i=0; i<q; i++){
            
            prev = listHead;
            preHead = listHead;
            listHead = node;
            for(int j=0; j<k; j++){
                preHead->next = node;
                listHead->next = node->next;
                if(j!=0)
                    node->next = prev;
                prev = node;
                node = listHead->next;
            }
            if(!headFlag){
                headFlag = true;
                rtn = prev;
            }
        }
        
        return rtn;
    }
};
