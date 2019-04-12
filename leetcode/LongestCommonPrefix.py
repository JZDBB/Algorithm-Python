
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    first = strs[0]
    del strs[0]
    char = list(first)
    ans = ''
    for i in range(len(char)):
        for item in strs:
            if first[0:i+1] == item[0:i+1]:
                continue
            else:
                return ans
        ans = first[0:i+1]
    return ans

def longestCommonPrefix2(strs):
    if len(strs) == 0:
        return ''
    ans = strs[0]
    del strs[0]
    for i in range(len(strs)):
        index = -1
        for j in range(len(ans)):
            try:
                if ans[j] == strs[i][j]:
                    index = j
                else:
                    break
            except:
                continue
        ans = ans[0:index+1]
    return ans

def longestCommonPrefix_fast(strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

def longestCommonPrefix_fast2(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1

print(longestCommonPrefix2(["dog","racecar","car"]))


"""
r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''

"""
