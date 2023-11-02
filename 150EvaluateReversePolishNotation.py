from typing import List


class Solution:
    exp = []

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        result = 0
        for t in tokens:
            if t in ['/', '*', '+', '-']:
                op1 = int(self.exp.pop())
                op2 = int(self.exp.pop())

                if t == '/':
                    result = op2 / op1
                elif t == '*':
                    result = op2 * op1
                elif t == '+':
                    result = op2 + op1
                else:
                    result = op2 - op1
                self.exp.append(result)
            else:
                self.exp.append(t)
        return int(result)


if __name__ == '__main__':
    print(Solution().evalRPN(["2","1","+","3","*"]))