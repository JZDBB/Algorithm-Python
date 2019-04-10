
def atoi(s):
    flag = True
    s = s.lstrip()
    ls = s.split(" ")
    num = 0
    ceil = list(ls[0])
    if ceil:
        if ceil[0] == "-":
            flag = False
            del ceil[0]
        elif ceil[0] == "+":
            del ceil[0]
        for i in ceil:
            try:
                a = int(i)
                num = num * 10 + a
            except:
                if flag:
                    if num > 2 ** 31 -1:
                        return 2 ** 31 -1
                    return num
                else:
                    if -num < - 2 ** 31:
                        return - 2 ** 31
                    return -num
        if flag:
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return num
        else:
            if -num < - 2 ** 31:
                return - 2 ** 31
            return -num
    else:
        return 0

print(atoi("-91283472332"))