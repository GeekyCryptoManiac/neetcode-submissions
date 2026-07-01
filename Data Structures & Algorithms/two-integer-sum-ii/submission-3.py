class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #sorted in increasing order i assume 
    # Ok so i will try another strategy, take 1 from left to right
    # so i will have a left variable and a right variable
        left = 0
        right = len(numbers) - 1 
        while left<=right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right + 1]
            elif numbers[left] + numbers[right] < target:
                left +=1
            elif numbers[left] + numbers[right] > target:
                right -=1

        
    