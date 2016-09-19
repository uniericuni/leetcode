class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        
        std::vector<vector<int>> ans(n, vector<int>(n));
        
        int uBound = 1, dBound = n-1, lBound = 0, rBound = n-1;
        int hAdder = 1, vAdder = 0, x = 0, y = 0;
        
        for(int i=1; i<n*n+1; i++){
            ans[y][x] = i;
            if(x==rBound && hAdder>0){
                rBound--;
                hAdder = 0;
                vAdder = 1;
            }
            else if(y==dBound && vAdder>0){
                dBound--;
                hAdder = -1;
                vAdder = 0;
            }
            else if(x==lBound && hAdder<0){
                lBound++;
                hAdder = 0;
                vAdder = -1;
            }
            else if(y==uBound && vAdder<0){
                uBound++;
                hAdder = 1;
                vAdder = 0;
            }
            x += hAdder;
            y += vAdder;
        }
        
        return ans;
    }
};
