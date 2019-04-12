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

def change_num_roman(num):
    """
    :type num: int
    :rtype s: str
    """
    ans = ''
    ans += 'M' * int(num // 1000)
    num = num % 1000
    ans += 'CM' * int(num // 900)
    num = num % 900
    ans += 'D' * int(num // 500)
    num = num % 500
    ans += 'CD' * int(num // 400)
    num = num % 400
    ans += 'C' * int(num // 100)
    num = num % 100
    ans += 'XC' * int(num // 90)
    num = num % 90
    ans += 'L' * int(num // 50)
    num = num % 50
    ans += 'XL' * int(num // 40)
    num = num % 40
    ans += 'X' * int(num // 10)
    num = num % 10
    ans += 'IX' * int(num // 9)
    num = num % 9
    ans += 'V' * int(num // 5)
    num = num % 5
    ans += 'IV' * int(num // 4)
    num = num % 4
    ans += 'I' * num
    return ans


def chang_num_roman_faster(num):
    ans = '' + \
          ["", "M", "MM", "MMM"][num // 1000] + \
          ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"][(num % 1000) // 100] + \
          ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"][num % 100 // 10] + \
          ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"][num % 10]
    return ans

# a = "MCMXCIV"
# print(change_roman_num(a))

print(change_num_roman(31))