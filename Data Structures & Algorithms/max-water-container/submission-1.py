class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #I have an array heights = []
        #heights[i] represents the height of the ith bar
        #[1,2,3,5]
        # so for example heights[3] means, bar number 4 has a height of 5
        #i assume water means volume? but looking at the picture its width x height
        #width being the distance of the bar 1 to bar 2 it seems

        tmp = 0
        current_max = 0

        i = 0
        left = i
        right = len(heights) -1

        while left<=right:
            selected_height = min(heights[left],heights[right])
            selected_width = right - left
            tmp = selected_height * selected_width
            maximum = max(tmp,current_max)
            current_max = maximum
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return current_max