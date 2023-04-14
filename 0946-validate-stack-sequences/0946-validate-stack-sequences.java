class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int j=0;
Stack<Integer> stack = new Stack<Integer>();
for(int i : pushed){
    stack.push(i);
    while(j<popped.length && !stack.isEmpty() && stack.peek()==popped[j]){
        stack.pop();
        j++;
    }
}
return stack.isEmpty();
        
    }
}