class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int n = s.length();
        int i=0, j=0, ans=0;
        int *list = new int[256];
        for(int k=0; k<128; k++)
            list[k] = n;
        
        while(i<n && j<n){
            int index = int(s[j]);
            if(list[index]!=n && i<=list[index])
                i = list[index]+1;
            list[index] = j;
            if(j-i+1 > ans)
                ans = j-i+1;
            j++;
        }
        
        return ans;
        
    }
};
