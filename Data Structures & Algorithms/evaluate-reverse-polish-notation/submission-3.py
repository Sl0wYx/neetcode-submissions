import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        stack = []

        for t in tokens:
            print(stack)
            if t in operators:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(operators[t](y,x)))
                continue
            stack.append(int(t))

        return stack[0]
            