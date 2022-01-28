def fact(inp:int):
    res = 1
    for i in range(1,inp + 1):
        res *= i
    return res

print(fact(int(input("input your number to compute the factorial for: "))))