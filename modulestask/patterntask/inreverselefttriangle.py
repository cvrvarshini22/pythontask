# inverselefttriangle.py

def inverselefttriangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)
