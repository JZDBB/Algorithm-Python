# 给定一个字符串，这个字符串里面只包含大中小括号,让你判断这个字符串是否合法，
# 所谓的括号合法指的就是左括号和右括号必须匹配，同时也允许嵌套到情况。

def inValid(s):
    stack = []
    paren_map = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

# 更简洁时间复杂度更低的方法见 closed_nesting.jpg