class Solution {
public:
    bool isPalindrome(string s) {
        
        if(s=="")
            return true;
            
        string sTemp;
        int len = s.length();
        char c;
        for(int i=0; i<len; i++){
            c = s[i];
            if(c<='Z' && c>='A'){
                sTemp.append(1,c-('A'-'a'));   
            }
            else if( (c<='z' && c>='a') || (c<='9' && c>='0') ){
                sTemp.append(1,c);
            }
        }

        len = sTemp.length();
        for(int i=0; i<(int(len/2)); i++){
            if( sTemp[i] != sTemp[len-i-1] )
                return false;
        }
        
        return true;
        
    }
};
