class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_vol = 0
        while left < right:
            current_height = min(height[left],height[right])
            if (current_height * (right-left)) > max_vol:
                max_vol = current_height * (right-left)
            if current_height == height[left]:
                left +=1
            else:
                right -=1
        return max_vol