class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == "+":
                st.append(int(st.pop()) + int(st.pop()))
            elif c == "-":
                sec,fir = int(st.pop()),int(st.pop())
                st.append(fir-sec)
            elif c == "*":
                st.append(int(st.pop()) * int(st.pop()))
            elif c == "/":
                sec,fir = st.pop(), st.pop()
                st.append(int(int(fir)/int(sec)))
            else:
                st.append(c)
        return int(st[0])
        