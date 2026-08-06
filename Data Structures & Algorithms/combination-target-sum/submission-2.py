class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        hashm = {}


        def backtrack(index, path): 
            sum_ = sum(path)
            if sum_ > target or index == len(nums):
                return
            
            if sum_ == target:
                if (tuple(sorted(path[:])) in hashm):
                    return
                hashm[tuple(sorted(path[:]))] = 1
                results.append(path[:])
                return
            
            # decision 1: include current index 
            path.append(nums[index])
            backtrack(index, path)

            path.pop()
            backtrack(index + 1, path)
        
        backtrack(0, [])
        return results

            
            
                