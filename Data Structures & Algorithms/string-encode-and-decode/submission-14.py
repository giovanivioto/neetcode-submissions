class Solution:
    def encode(self, strs: List[str]) -> str:
        my_string = ""
        for s in strs:
            my_string += f"{len(s)}#{s}"
        return my_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            sep = s[i:].find("#")
            lenght = s[i:][:sep]
            f = sep+1
            t = int(lenght)+len(lenght)+1
            result.append(s[i:][f:t])
            i += t
        return result