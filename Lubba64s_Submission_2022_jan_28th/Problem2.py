def repeatChar(char:str,times:int):
    res = ''
    for i in range(0,times):
        res += char
    return res

def printTri(inp:int, char:str):
    toPrint = repeatChar(char,inp)
    for i in range(0,inp):
        print(toPrint)
        toPrint = toPrint[0:-1]

def remove_items(list, item):
    res = [i for i in list if i != item]
    return res

_input = input("input the elements for the ranges you want to compute: ").split(' ')
_input = remove_items(_input,'')
for i in range(0,len(_input)):
    _input[i] = int(_input[i])
    printTri(_input[i],'.')
    print('')