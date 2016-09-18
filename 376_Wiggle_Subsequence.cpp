#include<algorithm>
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        
        if(nums.size()==0)
            return 0;
            
        int count = 1, flag = 0, prev = nums[0], ans = 0;
        for(int i=0; i<nums.size(); i++){
            if(prev>nums[i] && flag>=0){
                flag = -1;
                count++;
            } 
            else if(prev<nums[i] && flag<=0){
                flag = 1;
                count++;
            }
            ans = max(count, ans);
            prev = nums[i];
        }
        
        return ans;

    }
};
