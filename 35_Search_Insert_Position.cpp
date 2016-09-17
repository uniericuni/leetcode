#include<limits.h>
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        vector<int> list = nums;
        list.push_back(INT_MAX);
        
        int n;
        int low = 0;
        int top = list.size()-1;
        
        while(low != top){
            
            n = (top-low)/2;
            if(list[low+n] > target)
                top = low+n;
            else if(list[low+n+1] < target)
                low = low+n+1;
            else if(list[low+n] == target)
                return low+n;
            else
                return low+n+1;
            
        }
        
        return low;
        
    }
};
