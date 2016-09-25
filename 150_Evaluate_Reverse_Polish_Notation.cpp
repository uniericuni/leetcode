#include<stack>
#include<string>
#include<iostream>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        if(tokens.empty())
            return 0;
        
        int num1, num2, num;
        string item;
        std::stack<string> stk;
        for(int i=0; i<tokens.size(); i++){
            item = tokens[i];
            if(item=="+"){
                num2 = std::stoi(stk.top());
                stk.pop();
                num1 = std::stoi(stk.top());
                stk.pop();
                num = num1+num2;
                stk.push(std::to_string(num));
            }
            else if(item=="-"){
                num2 = std::stoi(stk.top());
                stk.pop();
                num1 = std::stoi(stk.top());
                stk.pop();
                num = num1-num2;
                stk.push(std::to_string(num));
            }
            else if(item=="*"){
                num2 = std::stoi(stk.top());
                stk.pop();
                num1 = std::stoi(stk.top());
                stk.pop();
                num = num1*num2;
                stk.push(std::to_string(num));
            }
            else if(item=="/"){
                num2 = std::stoi(stk.top());
                stk.pop();
                num1 = std::stoi(stk.top());
                stk.pop();
                num = num1/num2;
                stk.push(std::to_string(num));
            }
            else
                stk.push(item);
        }
        
        return std::stoi(stk.top());
        
    }
};
