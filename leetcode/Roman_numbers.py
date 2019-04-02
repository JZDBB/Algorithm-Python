def change_roman_num(s):
    """
    :type s: str
    :rtype: int
    """
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
            ans -= a[s[i]]
        else:
            ans += a[s[i]]
    return ans

a = "MCMXCIV"
print(change_roman_num(a))