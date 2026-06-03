class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Left pass: output[i] = product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Right pass: multiply output[i] by product of everything to the RIGHT of i
        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output