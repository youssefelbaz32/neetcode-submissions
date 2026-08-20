class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        res = [1] * len(nums)

        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        # pre = [1] * len(nums)

        # post = [1] * len(nums)
        
        # res = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     pre[i] = pre[i - 1] * nums[i - 1]
        #     # [1, 2, 4, 6]
        #     # [1, 1, 2, 8]


        # for i in range(len(nums) - 2, -1, -1):
        #     post[i] = post[i + 1] * nums[i + 1]
        #     # [1, 2, 4, 6]
        #     # [48, 24, 6, 1]
        

        # for i in range(len(nums)):
        #     res[i] = pre[i] * post[i]
        
        return res