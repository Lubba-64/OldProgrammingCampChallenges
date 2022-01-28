ORIGIN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TO =     'DJPGOAQWHCTLZXSBVYUFNRMIKE'

def encodeChars(inp):
    res = ''
    for char in inp:
        replaced = False
        for i in range(0,len(ORIGIN)):
            if (ORIGIN[i] == char):
                res += TO[i]
                replaced = True
                break
            if (ORIGIN[i].lower() == char):
                res += TO[i].lower()
                replaced = True
                break
        if (not replaced):
            res += char
    return res

def encodeNumbers(inp:str):
    res = ''
    for char in inp:
        if (not char.isdigit()):
            res += char
            continue
        res += str((int(char)+3) % 10)
        pass
    return res



inp = input('thing to encode: ')

print(encodeNumbers(encodeChars(inp)))
