# Valid Parentheses
Table of Contents:
- [Valid Parentheses](#valid-parentheses)
  - [Problem Statement:](#problem-statement)
  - [Examples:](#examples)
  - [Solution Approach:](#solution-approach)

## Problem Statement:
Given a string that may consist of opening and closing parentheses, your task is to check if the string contains valid parenthesization or not.

The conditions to validate are:

    Every opening parenthesis should be closed by the same kind of parenthesis. So, {)and [(]) strings are invalid.

    Every opening parenthesis must be closed in the correct order. So, )( and ()(() are invalid.

Constraints:

    1 ≤ string.length ≤10^4
    The string will only contain the following characters: (, ), [, ], { and }.

## Examples:
| Input  |  Output |
|---|---|
|  {([])} | True  |
|  ()[]{} | True  |
|  (}[]() | False  |
|  {) | False  |
|  [(]) | False  |
|  ()(() | False  |
|  )( | False  |
|  ( | False  |
|  ) | False  |


## Solution Approach:
The solution is implemented in python3. The solution is based on the concept of stack. The solution is implemented in the following steps:
1. Create a stack.
2. Iterate over the string.
3. If the current character is an opening bracket, push it into the stack.
4. If the current character is a closing bracket and matches as a closing bracket to the top element of the stack, pop the top element from the stack.
5. If the current character is a closing bracket and does not match as a closing bracket to the top element of the stack, return False.
6. If the stack is empty after the iteration, return True. Else, return False.
