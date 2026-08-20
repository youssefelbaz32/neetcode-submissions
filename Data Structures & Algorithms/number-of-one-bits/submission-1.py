class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        while n:
            n = n & (n - 1)
            cnt += 1
        
        return cnt
        # for i in range(32):
        #     if (n & 1):
        #         cnt += 1
        #     n = n >> 1
        
        # return cnt

        