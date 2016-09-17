nclude<algorithm>

class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int ans = 0, area;
        int i = 0;
        int j = height.size()-1;
        
        while(j>i){
            area = (j-i)*min(height[i], height[j]);
            ans = max(area, ans);
            if(height[i]<height[j])
                i++;
            else
                j--;
        }        
        return ans;
    }
};
