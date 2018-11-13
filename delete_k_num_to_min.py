def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    list_num = list(num)
    list_result = []
    curr = list_num.pop(0)
    list_result.append(curr)
    count = 0
    if k == 0:
        return num
    for i in range(len(list(num))):
        if (list_num):
            next = list_num.pop(0)
        else:
            next = '0'

        if curr > next:
            list_result.append(next)
            count += 1
        elif curr == next:
            list_result.append(next)
        else:
            list_result.append(curr)
            list_result.append(next)
        if count >= k:
            break
        curr = list_result.pop()
    list_result.extend(list_num)
    str_result = "".join(a for a in list_result)
    a = int(str_result)
    str_result = str(a)
    return str_result

if __name__ == '__main__':
    a = removeKdigits("112", 1)
    print(a)