def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    list_num = list(num)
    list_result = []
    curr = list_num.pop(0)
    if k == 0:
        return num
    for i in range(k):
        if (list_num):
            next = list_num.pop(0)
        else:
            next = '0'
            list_result.append(next)
        if curr > next:
            try:
                list_result.pop()
                list_result.append(next)
            except:
                list_result.append(next)
        else:
            try:
                list_result.pop()
                list_result.append(curr)
            except:
                list_result.append(curr)
        curr = list_result[-1]
    list_result.extend(list_num)
    str_result = "".join(a for a in list_result)
    a = int(str_result)
    str_result = str(a)
    return str_result

if __name__ == '__main__':
    a = removeKdigits("112", 1)
    print(a)