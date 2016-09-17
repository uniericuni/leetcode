class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        
        int i=0, j=0, sum=0, ans=nums.size()+1;
        
        while(i<=j){
            if(sum>=s){
                ans = (ans<j-i)? ans:j-i;
                sum -= nums[i];
                i++;
            }
            else{
                if(j>=nums.size())
                    break;
                sum += nums[j];
                j++;
            }
        }
        
        if(ans>nums.size())
            return 0;
        else
            return ans;
                
    }
};
