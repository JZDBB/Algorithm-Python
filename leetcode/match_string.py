def isMatch(s, p):
    list_s = list(s)
    list_p = list(p)
    for c in list_p:
        if c == "." or c == list_s[0]:
            pass


print(isMatch("aa", "a*"))