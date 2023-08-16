def isValidBracket(s: str) -> bool:
    #若str为奇数，表示无法匹配，直接返回false
    if len(s) % 2 == 1:
        return False

    #定义字典，把有括号映射到相应左括号
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    #初始化 空栈 (先进后出)：存储左括号
    stack = list()

    #遍历str的每个character
    for c in s:
        # 如果c是右括号
        if c in pairs:
            # 如果 
            # 1.栈是空的(说明现在有一个右括号，但是之前并没有匹配的左括号) 
            # or 
            # 2.栈非空， 但栈的顶端（最后进入的左括号）和当前右括号的影射不匹配
            # 都返回False
            if not stack or stack[-1] != pairs[c]:
                return False
            # 匹配成功，弹出栈顶左括号
            stack.pop()
        else:
            # c是右括号，压入栈中
            stack.append(c)
    # 遍历结束后栈为空，表示都匹配成功。
    return not stack

s = "()[]{}"
print(isValid(s))
