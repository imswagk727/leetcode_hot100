def longestSubstring(s: str) -> int:
    if not s:
        return 0
    left = 0  # 窗口左侧起始
    lookup = set()  # 当前窗口有哪些元素
    n = len(s)
    max_len = 0  # 窗口最大长度
    cur_len = 0  # 当前窗口长度
    for i in range(n):
        cur_len += 1  # 窗口的右端往右侧滑动一个

        # abcw wekab
        # lookup[a,b,c,w]
        # cur_len 5
        # -1 -1 -1 -1
        # lookup[]
        # lookup.add
        # lookup[w]
        # now curlen=1
        while s[i] in lookup:  # 如果新来的这个s[i]在lookup中已经出现过
            lookup.remove(s[left])
            # 窗口左端收缩一格

            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len


print(longestSubstring("abcabcbb"))
