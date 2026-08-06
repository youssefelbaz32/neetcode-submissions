class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = int((high + low)/2)
#or mid = low+ int((high - low) /2)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high =  mid -1
            if target == nums[mid]:
                return mid
        
        return -1        