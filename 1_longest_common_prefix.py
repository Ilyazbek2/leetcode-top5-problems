"""
Problem: Longest Common Prefix
LeetCode: https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(s.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
