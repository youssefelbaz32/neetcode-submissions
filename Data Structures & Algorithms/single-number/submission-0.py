class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total_xor = 0
        for i in range(len(nums)):
            total_xor ^= nums[i]
        return total_xor


        