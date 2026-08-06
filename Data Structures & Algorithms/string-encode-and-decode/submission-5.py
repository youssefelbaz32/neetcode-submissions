class Solution:

    def encode(self, strs: List[str]) -> str:
        # we can use :;: to seperate
        if len(strs) == 0:
            return "empty"
        ans = ""
        for i in range(len(strs)):
            ans += strs[i]
            if (i != len(strs) - 1) :
                ans += ":;:"
        return ans


    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split(":;:")
