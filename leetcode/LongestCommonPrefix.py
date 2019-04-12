
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

print(longestCommonPrefix2(["dog","racecar","car"]))
