import ast
import operator
import os

def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression."""
    try:
        # A simple and safe evaluator for basic math expressions
        def eval_expr(expr):
            ops = {
                ast.Add: operator.add, ast.Sub: operator.sub,
                ast.Mult: operator.mul, ast.Div: operator.truediv,
                ast.Pow: operator.pow, ast.BitXor: operator.xor,
                ast.USub: operator.neg
            }
            def eval_(node):
                if isinstance(node, ast.Constant):
                    return node.value
                elif isinstance(node, ast.BinOp):
                    return ops[type(node.op)](eval_(node.left), eval_(node.right))
                elif isinstance(node, ast.UnaryOp):
                    return ops[type(node.op)](eval_(node.operand))
                else:
                    raise TypeError(node)
            return eval_(ast.parse(expr, mode='eval').body)

        result = eval_expr(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def write_file(arguments: str) -> str:
    """Write text to a file. Arguments should be separated by a pipe '|', like 'filename.txt|content'."""
    try:
        parts = arguments.split('|', 1)
        if len(parts) != 2:
            return "Error: arguments must be in the format 'filename|content'."
        filename = parts[0].strip()
        content = parts[1]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing file: {e}"

# Tool registry
TOOLS = {
    "calculator": calculator,
    "write_file": write_file
}

if __name__ == "__main__":
    print(calculator("5 + 3 * 2"))
    print(write_file("test.txt|Hello World"))
