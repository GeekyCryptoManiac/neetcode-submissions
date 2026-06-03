class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        sequence_hold = 1
        for num in hash_set:
            if num - 1 not in hash_set:
                sequence_counter = 1
                current = num
                while (current + 1) in hash_set:
                    sequence_counter += 1
                    current += 1
                sequence_hold = max(sequence_hold, sequence_counter)
        
        return sequence_hold