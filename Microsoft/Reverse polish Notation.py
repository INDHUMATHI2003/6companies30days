class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for a in tokens:
            if a not in {"/","*","+","-"}:
                stack.append(int(a))
            else:
                r = stack.pop()
                l = stack.pop()
                if a == '+':
                    stack.append(l + r)
                elif a == '-':
                    stack.append(l - r)
                elif a == '*':
                    stack.append(l * r)
                elif a == '/':
                    stack.append(int(l / r))
        return stack[0]

        

            
