# 20. Valid Parentheses
# Easy
# 19.8K
# 1.2K
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                if char == "}" and stack [-1] != "{":
                    return False

                stack.pop()
        return len(stack) == 0

solution = Solution()
print(solution.isValid("()"))  # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))  # False
print(solution.isValid("([)]"))  # False
print(solution.isValid("{[]}"))  # True
