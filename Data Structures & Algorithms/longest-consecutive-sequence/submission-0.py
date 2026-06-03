class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_set = sorted(set(nums))
        sequence_counter = 1
        sequence_hold = 1
        for i in range(len(sorted_set) - 1):
            if sorted_set[i] + 1 == sorted_set[i + 1]:
                sequence_counter += 1
            else:
                sequence_hold = max(sequence_hold, sequence_counter)
                sequence_counter = 1
        
        return max(sequence_hold, sequence_counter)