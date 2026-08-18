class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hashm = dict()

        hashm["("] = ")"
        hashm["{"] = "}"
        hashm["["] = "]"
        
        for i in s:
            if i in hashm.keys():
                stack.append(i)
            elif i in hashm.values():
                if not stack or hashm[stack.pop()] != i:
                    return False
        
        if stack:
            return False
        
        return True

        