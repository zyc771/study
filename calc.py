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

print(add(1, 2))
print(subtract(5, 3))
print(multiply(3, 4))