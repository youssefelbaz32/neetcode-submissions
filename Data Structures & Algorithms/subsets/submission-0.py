class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(index, path):
            if (index == len(nums)):
                results.append(path[:])
                return
            
            #decision 1 -> include the number at the index
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        return results
