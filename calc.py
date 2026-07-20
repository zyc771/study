def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：不能除以0"
    return a / b

print(f"1 + 2 = {add(1, 2)}")
print(f"5 - 3 = {subtract(5, 3)}")
print(f"3 × 4 = {multiply(3, 4)}")
print(f"5 / 0 = {divide(5, 0)}")