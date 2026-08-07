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
            
            sum_ = recurse(curr + 1) + recurse(curr + 2)

            memo[curr] = sum_

            return sum_
        
        return recurse(0)


        