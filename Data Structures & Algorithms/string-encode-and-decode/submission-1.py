class Solution:
    def encode(self, strs: List[str]) -> str:
        my_key = ""
        for s in strs:
            my_key += f"{len(s)}#{s}"
        return my_key + f"_end_{len(strs)}_end_"

    def decode(self, s: str) -> List[str]:
        first_index_final = s.find("_end_")
        s = s.replace(s[first_index_final:], "")
        result=[]
        while s:
            my_word_lenght = s[:s.find("#")]
            my_word = s[s.find("#")+1:s.find("#")+1+int(my_word_lenght)]
            result.append(my_word)
            s = s[len(my_word_lenght)+1+len(my_word):]
        return result