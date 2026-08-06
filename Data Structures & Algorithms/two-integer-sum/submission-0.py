class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            num_required = target - nums[i]
            for j in range(i + 1, len(nums)):
                if num_required == nums[j]:
                    return [i,j]
        