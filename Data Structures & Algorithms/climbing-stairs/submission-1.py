class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def recurse(curr):

            if curr > n:
                return 0
            if curr == n:
                return 1
            if curr in memo:
                return memo[curr]
            
            step1 = recurse (curr + 1)
            step2 = recurse (curr + 2)

            memo[curr] = step1 + step2

            return step1 + step2 
        
        return recurse(0)


        