class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s += '+'
        st = []
        num = 0
        op = '+'
        # num = ''
        for i in s:
            if i.isdigit():
                num = int(i)
            else:
                num = int(num)
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    st.append(st.pop()*num)
                elif op == '/':
                    st.append(int(st.pop()/num))
                # num = ''
                num = 0
                op = i
        return sum(st)


solve = Solution()
s = "3+2/5*2"
print(solve.calculate(s))
