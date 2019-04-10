
def atoi(s):
    flag = True
    s = s.replace(" ", '')
    ls = list(s)
    num = 0
    if ls:
        if ls[0] == "-":
            flag = False
            del ls[0]
        elif ls[0] == "+":
            del ls[0]
        for i in range(len(ls)):
            try:
                a = int(ls[i])
            except:
                if flag:
                    if num > 2 ** 31 - 1:
                        return 2 ** 31 - 1
                else:
                    if -num < - 2 ** 31:
                        return -2 ** 31

                return num if flag == True else -num

            num = num * 10 + a
        if flag:
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
        else:
            if -num < - 2 ** 31:
                return -2 ** 31
    else:
        return 0

    return num if flag == True else -num

print(atoi("  0000000000012345678"))