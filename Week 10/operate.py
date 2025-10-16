def operate(func, a, b):
    return func(a, b)

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else None

# Example
print(operate(mul, 5, 6))  # Output: 30
