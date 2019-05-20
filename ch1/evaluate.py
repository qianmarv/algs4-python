"""
Arithmetic expression evaluation.
Assumption:
1. expression string is fully parenthesised
2. operaters and operands are separated by space
3. expression string is valid
"""


def evaluate(str):
    ops = []
    vals = []
    str_arr = str.split()
    for c in str_arr:
        # print("current c = %s" % c)
        if c == "+":
            ops.append(c)
        elif c == "-":
            ops.append(c)
        elif c == "*":
            ops.append(c)
        elif c == "/":
            ops.append(c)
        elif c == ")":
            val2 = vals.pop()
            val1 = vals.pop()
            op = ops.pop()
            if op == "+":
                vals.append(val1 + val2)
            elif op == "-":
                vals.append(val1 - val2)
            elif op == "*":
                vals.append(val1 * val2)
            elif op == "/":
                vals.append(val1 / val2)
            else:
                pass
        elif c == "(":
                pass
        else:
            vals.append(float(c))

    return vals[0]

if __name__ == "__main__":
    import sys
    expr = sys.argv[1]
    print( "%s = %f" % (expr, evaluate(expr)))
