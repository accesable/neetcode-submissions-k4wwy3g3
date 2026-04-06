class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            n = len(i)
            res += f"#{n}#{i}"
        return res
            

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i, j = 0, 1
        # is_delimeter = True
        while j < len(s) :
            l = 0
            if s[j] == '#' :
                # is_delimeter = not is_delimeter
                print(i,j)
                l = int(s[i+1:j])
                res.append(s[j+1: j+1+l])
                i = j + l + 1
                j = i + 1
                # continue
            j += 1

        return res
