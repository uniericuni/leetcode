#include<stack>
class Solution {
public:
    bool isValid(string s) {
        
        std::stack<char> list;
        char c, e='0';
        
        for(int i=0; i<s.length(); i++){
            c = s[i];
            if(c=='('||c=='['||c=='{'){
                list.push(c);
            }
            else if(c==')'||c==']'||c=='}'){
                if(list.empty())
                    return false;
                e = list.top();
                list.pop();
                if(e=='('&&c==')')
                    continue;
                else if(e=='['&&c==']')
                    continue;
                else if(e=='{'&&c=='}')
                    continue;
                else
                    return false;
            }
        }
        
        if(list.empty())
            return true;
        else
            return false;
    }
};
