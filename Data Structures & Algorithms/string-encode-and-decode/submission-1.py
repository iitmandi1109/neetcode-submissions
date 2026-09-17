class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Move after '#'
            i = j + 1

            # Extract string
            result.append(s[i:i + length])

            # Move to next encoded string
            i += length

        return result