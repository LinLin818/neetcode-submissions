from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        n = len(heights)
        stack = []  # indices, heights increasing from bottom to top

        for i in range(n):
            # bar i is shorter than the top, so the top has found its right boundary
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                height = heights[top]
                left = stack[-1] if stack else -1   # first shorter bar on the left
                width = i - left - 1                # bars strictly between left and i
                best = max(best, height * width)
            stack.append(i)

        # leftovers never met a shorter bar on the right, so their boundary is n
        while stack:
            top = stack.pop()
            height = heights[top]
            left = stack[-1] if stack else -1
            width = n - left - 1
            best = max(best, height * width)

        return best