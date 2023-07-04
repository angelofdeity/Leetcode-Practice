# Valid Parentheses
leetcode link [here](https://leetcode.com/problems/valid-parentheses/)

Table of Contents:
- [Valid Parentheses](#valid-parentheses)
  - [Problem Statement:](#problem-statement)
  - [Examples:](#examples)

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

