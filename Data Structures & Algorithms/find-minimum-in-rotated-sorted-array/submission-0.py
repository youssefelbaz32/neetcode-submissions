class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        low = 0
        high = len(nums) - 1
        ans = nums[-1]

        while (low <= high):
            mid = (low + high) // 2

            if (nums[mid] > ans):
                low = mid + 1
            elif (nums[mid] < ans):
                ans = nums[mid]
                high = mid - 1
            else:
                return ans
        return ans


        

        
        