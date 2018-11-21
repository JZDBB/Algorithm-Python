
def Wig_Subsq(num):
    if len(num) < 2:
        return len(num)
    dp = num[1] - num[0]
    if dp == 0:
        res = 1
    else:
        res = 2
    for i in range(len(num) - 2):
        temp = num[i+2] - num[i+1]
        if (temp*dp < 0 | (dp == 0 & temp != 0)):
            res += 1
        dp = temp

    return res

if __name__ == '__main__':
    a = Wig_Subsq([1, 2, 1, 4, 5, 6])
    print(a)