class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[right] > target and nums[right] >= nums[mid]:
                    right = mid - 1
                elif nums[right] > target and nums[right] < nums[mid]:
                    left = mid + 1
                elif nums[right] < target:
                    right = mid -1
                elif nums[right] == target:
                    return right
                else:
                    return -1  
            elif nums[mid] < target:
                if nums[left] < target and nums[left] <= nums[mid]:
                    left = mid + 1
                elif nums[left] < target and nums[left] > nums[mid]:
                    right = mid - 1
                elif nums[left] == target:
                    return left
                elif nums[left] > target:
                    left = mid + 1
                else:
                    return -1  
        return -1
