class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        tracker = {}
        s = s.strip()

        if len(s) % 2 != 0:
            return False

        tracker["["] = "]"

        tracker["{"] = "}"
        tracker["("] = ")"

        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            else:
                if stack and tracker[stack[-1]] != s[i]:
                    return False
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
                    
        if len(stack) != 0:
            return False   

        return True
        