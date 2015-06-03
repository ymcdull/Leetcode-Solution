class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        n = len(height)
        l = 0
        r = n - 1
        res = -1
        while l < r:
            res = max(res, (r-l) * min(height[l],height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
