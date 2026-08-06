class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 1, 2, 3


        # idx = 0

        #
        res = []


        def dfs(index, path):

            if index == len(nums):
                if len(path) == len(nums):
                    res.append(path[:])
                else:
                    return
            

            for choice in nums:
                if choice in path:
                    continue
                
                path.append(choice)
                dfs(index + 1, path)
                path.pop()
            

        dfs(0, [])
        return res

                
            
            

        