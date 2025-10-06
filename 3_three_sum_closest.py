"""
Problem: 3Sum Closest
LeetCode: https://leetcode.com/problems/3sum-closest/
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))  # Output: 2
    print(s.threeSumClosest([0,0,0], 1))      # Output: 0
