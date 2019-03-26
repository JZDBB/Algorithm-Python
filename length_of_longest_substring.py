

def LongestSubstring(str):
    """
    :param str: A string
    :return: Longest str for input which has not same letters.
    """
    left = 0
    right = 1
    cur = []
    num = 0
    str_list = list(str)
    while(True):
        if cur:
            cur.append(str_list[right-1])
        if str_list[right] in cur:
            num = max(num, len(cur))
            id = cur.index(str_list[right])
            left += id + 1
            for i in range(id):
                del cur[i]
        cur.append(right)
        right += 1
        if right >= len(str_list):
            return num


if __name__ == '__main__':
    str = "shaldfhwelkjdh"
    print(LongestSubstring(str))
