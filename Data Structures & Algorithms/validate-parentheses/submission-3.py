class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(": ")", "[": "]", "{": "}"}
        st = []
        for i in s:
            if i in m:
                st.append(i)
            else:
                if len(st) > 0:
                    x = st.pop()
                    if m[x] != i:
                        return False
                else :
                    return False
        return len(st) == 0
