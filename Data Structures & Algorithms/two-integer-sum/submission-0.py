class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:  # Check first
                return [seen[complement], i]
            
            seen[nums[i]] = i  # Then add current element