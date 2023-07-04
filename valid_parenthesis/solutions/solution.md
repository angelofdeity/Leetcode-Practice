## Solution Approach:
The solution is implemented in python3. The solution is based on the concept of stack. The solution is implemented in the following steps:
1. Create a stack.
2. Iterate over the string.
3. If the current character is an opening bracket, push it into the stack.
4. If the current character is a closing bracket and matches as a closing bracket to the top element of the stack, pop the top element from the stack.
5. If the current character is a closing bracket and does not match as a closing bracket to the top element of the stack, return False.
6. If the stack is empty after the iteration, return True. Else, return False.
