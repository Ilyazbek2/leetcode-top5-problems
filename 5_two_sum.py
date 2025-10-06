"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))  # Output: [0,1]
