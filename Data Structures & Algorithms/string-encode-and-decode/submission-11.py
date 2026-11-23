class Solution:
    def encode(self, strs: List[str]) -> str:
        my_key = []
        for s in strs:
            my_key.append(f"{len(s)}#{s}")
        return "".join(my_key)

    def decode(self, s: str) -> List[str]:
        result=[]
        pointer_one, pointer_two = 0, 0
        while pointer_one < len(s):
            while s[pointer_one+pointer_two:(pointer_one+pointer_two+1)] != '#':
                pointer_two += 1
            my_length = int(s[pointer_one:pointer_one+pointer_two])
            begin = pointer_one+pointer_two+1
            finish = begin + my_length
            my_string = s[begin:finish]
            result.append(my_string)
            pointer_one+=my_length+pointer_two+1
            pointer_two=0
        return result