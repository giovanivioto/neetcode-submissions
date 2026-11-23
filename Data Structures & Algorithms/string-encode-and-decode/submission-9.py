class Solution:
    def encode(self, strs: List[str]) -> str:
        my_key = []
        for s in strs:
            my_key.append(f"{len(s)}#{s}")
        return "".join(my_key)

    def decode(self, s: str) -> List[str]:
        result=[]
        while s:
            my_word_lenght = s[:s.find("#")]
            my_word = s[s.find("#")+1:s.find("#")+1+int(my_word_lenght)]
            result.append(my_word)
            s = s[len(my_word_lenght)+1+len(my_word):]
        return result