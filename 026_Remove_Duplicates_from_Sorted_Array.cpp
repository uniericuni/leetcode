class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int prev = NULL, count = 0, len = nums.size();
        
        for(int i=0; i<len; i++){
            if(i==0 || prev!=nums[0]){
                count++;
                nums.push_back(nums[0]);
                prev = nums[0];
            }
            nums.erase(nums.begin());
        }
        return count;
        
    }
};
