class Solution {
public:
    int mySqrt(int x) {
        
        double n = x, half = x/2, prev;
        while(n*n != x){
            
            prev = n;
            if(n*n<x)
                n = n+half;
            else
                n = n-half;
            half /= 2;
            if(int(prev)==int(n))
                break;
            
        }
        
        unsigned int m = int(n);
        if(m*m>x)
            m--;
        else if((m+1)*(m+1)<=x)
            m++;
            
        return m;
        
    }
};
