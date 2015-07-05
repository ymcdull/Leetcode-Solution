class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        for i in xrange(len(tokens)):
            token = tokens[i]
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    # Add special judgment for devision in Python
                    if a*b >= 0:
                        stack.append(a/b)
                    else:
                        stack.append(-((-a)/b))
        return stack.pop()
