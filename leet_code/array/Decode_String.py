class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ele in s:

            # If we find opening bracket then we combine digits to build number
            if ele == '[':
                cur = ''
                while len(stack) and stack[-1].isdigit():
                    last = stack.pop()
                    cur = last + cur

                stack.append(cur)
                stack.append(ele)
            # If we find closing bracket then we combine characters
            elif ele == ']':
                repeat = ''
                while stack[-1] != '[':
                    repeat = stack[-1] + repeat
                    stack.pop()

                # Once characters are combined then we multiply it with our number
                bracket = stack.pop()
                numb = stack.pop()
                stack.append(int(numb) * repeat)
            else:
                stack.append(ele)

        return ''.join(stack)

s = "3[a]2[bc]"
#s = "3[a2[c]]"
res = Solution().decodeString(s)
print(res)
