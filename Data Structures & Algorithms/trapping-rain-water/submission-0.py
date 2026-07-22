class Solution:
    def trap(self, height: List[int]) -> int:
        #Positive integer array only
        #okay so water can only be trapped if its caught in between any 2 bars
        #we should calculate the area of water by the individual squares that it takes up and sum it
        #so for a list [2,5,7,8] i can ignore what ever is the most left and most right
        #Beginning the comparison between the first 2 index then the next 2 and the next 2 
        #oo but the catch is, water can only go in if there's a 0 in between actually so its not necesarily the next 2
        #We should see which positions this 0s are in
        #oo but heres a case for list say [3,0,1,2,4]
        # i cant just compare 3 and 1 as theyre between 0, because eventually when it reaches to 4, the area will grow from 1 to 3 to to 6
        # so how i see it is that, whatever that is between this 0s, ill have to watch whichever is bigger or same as 3, and only if there is the area from 3 to that to that next number can be "closed"

        #should i define the pointers as, where is 0? and the left right is what is left and right of that 0, then the if cases happens after
        # using the same list for example
        # l = height[0] r = height[2], add this to global area
        #now we know 3>1 so pointer right move 1
        # is next pointer > l ? if not, add area  till we hit a bigger or same pointer

        n = len(height)
        total_water = 0

        for i in range(n):
            # scan everything to the left of i
            max_left = 0
            for j in range(0, i):
                max_left = max(max_left, height[j])

            # scan everything to the right of i
            max_right = 0
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])

            # water level above index i, capped at 0 if negative
            water_level = min(max_left, max_right)
            water_here = water_level - height[i]
            if water_here > 0:
                total_water += water_here

        return total_water