
def Z_trans(s, numRows):
    """
    :param str: A string for trans.
    :return res: a result for z-transform
    """
    if numRows < 2:
        return s
    ls, div = range(len(s)), 2 * numRows - 2
    res_l = ['' for i in range(numRows)]
    for i in ls:
        p = i % div
        p = p if p < numRows else div - p
        res_l[p] += s[i]

    return ''.join(res_l)


def Z_trans_slow(s, numRows):
    out = ['' for i in range(numRows)]
    t = 0
    while t < len(s):
        for i in range(0, numRows):
            out[i] += s[t]
            t += 1
            if t == len(s):
                break
        if t == len(s):
            break
        for i in range(numRows - 2, 0, -1):
            out[i] += s[t]
            t += 1
            if t == len(s):
                break
    res = ''.join(out)
    return res

