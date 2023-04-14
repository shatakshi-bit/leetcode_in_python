class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int j=0;
std::stack<int> stack;
for(int i : pushed){
    stack.push(i);
    while(j<popped.size() && !stack.empty() && stack.top()==popped[j]){
        stack.pop();
        j++;
    }
}
return stack.empty();
    }
};