class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 1, 2, 3


        # idx = 0

        #
        res = []
        used = [False] * len(nums)


        def dfs(path):

            if len(path) == len(nums):
                res.append(path[:])
            

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                dfs(path)

                used[i] = False
                path.pop()
            

        dfs([])
        return res

                
            
            

        