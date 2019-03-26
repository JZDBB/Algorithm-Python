

def LongestSubstring(str):
    """
    :param str: A string
    :return: Longest str for input which has not same letters.
    """
    if str == None:
        return
    left = 0
    right = 1
    cur = []
    num = 0
    member = 0
    str_list = list(str)
    flag = False
    if str_list:
        pass
    else:
        return 0
    if len(str_list) == 1:
        return 1
    while(True):
        if cur:
            pass
        else:
            cur.append(str_list[right-1])
            member += 1
        if str_list[right] in cur:
            flag = True
            num = max(num, len(cur))
            id = cur.index(str_list[right])
            left += id + 1
            for i in range(id+1):
                del cur[0]
        cur.append(str_list[right])
        member += 1
        right += 1
        if right >= len(str_list):
            if flag:
                num = max(num, len(cur))
                return num
            else:
                return member

# 改进版
def LongestSubstring2(s):
    start = maxLength = 0
    usedChar = {}
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChar[s[i]] = i
    return maxLength


if __name__ == '__main__':
    str = "aab"
    print(LongestSubstring2(str))
