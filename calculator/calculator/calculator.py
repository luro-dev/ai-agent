import sys
import re

def calculate(expression):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        return 0

    tokens = re.findall(r'(\d+|[+\-*/])', expression)
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        token = tokens[i].strip()
        if token.isdigit():
            values.append(int(token))
        elif token in ['+', '-', '*', '/']:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(token):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.append(token)
        i += 1

    while len(ops) != 0:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    return values[-1]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        print(calculate(expression))
    else:
        print("Please provide an expression as a command-line argument.")