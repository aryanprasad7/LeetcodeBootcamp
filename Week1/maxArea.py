class Solution:
    def maxArea(self, height: List[int]) -> int:
        marea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            marea = max(marea, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return marea