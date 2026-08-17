class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def check_valid_bounds(stri):
            if ord(stri) >= ord("A") and ord(stri) <= ord("Z"):
                return True
            
            if ord(stri) >= ord("a") and ord(stri) <= ord("z"):
                return True
            
            if ord(stri) >= ord("0") and ord(stri) <= ord("9"):
                return True
            
            return False

        while l < r:
            if not check_valid_bounds(s[l]): 
                l += 1
                continue
            if not check_valid_bounds(s[r]): 
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

        