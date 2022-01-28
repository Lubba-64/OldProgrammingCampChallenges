def gaussSum(inp:int):
    res = 0
    for i in range(1,inp + 1):
        res += i    
    return res

print(gaussSum(int(input("input your number to compute the gauss sum for: "))))