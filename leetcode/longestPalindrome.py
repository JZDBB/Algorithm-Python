
def longestPalindrome(s):
    """
    :param s: A string
    :return nums: longest palindrome numbers
    """
    list_s = list(s)
    nums = 0
    res_list = []
    if len(list_s) == 0:
        return s
    if len(list_s) == 1:
        return s
    for i in range(len(list_s)):
        res = []
        for j in range(i + 1):
            res.insert(0, list_s[i - j])
            rev = list(res)
            rev.reverse()
            if res == rev:
                if nums < len(res):
                    nums = len(res)
                    res_list = list(res)
    return ''.join(b for b in res_list)

def longestPalindrome2(s):
    n = len(s)
    if n < 2 or s == s[::-1]:
        return s
    max_len = 1
    start = 0
    for i in range(1, n):
        even = s[i - max_len:i + 1]
        odd = s[i - max_len - 1:i + 1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]

print(longestPalindrome2("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"))
