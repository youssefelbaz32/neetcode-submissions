class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def twosum(start, target):

            l = start
            r = len(nums) - 1
            result_in = []

            while l < r: 
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    result_in.append([-1 * target, nums[l], nums[r]])
                    l += 1
                    while (nums[l -1] == nums[l]) and l < r:
                        l += 1

            return result_in
        
        results = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -1 * nums[i]
            two_ = twosum(i + 1, target)

            for j in range(len(two_)):
                if len(two_[j]) > 0:
                    results.append(two_[j])
            
        
        return results







        
            



        