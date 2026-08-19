class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(string)}/{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i

            # Find the "/" after the length
            while s[j] != "/":
                j += 1

            length = int(s[i:j])

            # String begins immediately after "/"
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end

        return result
