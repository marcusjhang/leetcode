class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            currentArea = h * w

            if currentArea > maxArea:
                maxArea = currentArea

            if (height[left]) < (height[right]):
                left += 1
            else:
                right -= 1

        return maxArea
    
# T O(n), S O(1)