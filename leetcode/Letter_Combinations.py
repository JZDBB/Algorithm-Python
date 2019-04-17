
def letterCombinations(digits):
    lettertab = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = []
    if not digits:
        return result
    findCombinations(digits, 0, '', result, lettertab)
    return result

# 递归调用
def findCombinations(digits, index, s, result, lettertab):
    if index == len(digits):
        result.append(s)
        return
    char = digits[index]
    letters = lettertab[int(char)]
    if not letters:
        findCombinations(digits, index + 1, s, result, lettertab)
    for letter in letters:
        findCombinations(digits, index + 1, s + letter, result, lettertab)


print(letterCombinations("23"))