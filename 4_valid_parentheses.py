"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))   # True
    print(s.isValid("(]"))       # False
