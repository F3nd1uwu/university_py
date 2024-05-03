def bunny(start, finish, length):
    def check(cur, jumps, path, res):
        if jumps == 0:
            if cur == finish:
                res.append(path.copy())
            return
        if jumps != 0 and cur == finish:
            return

        path.append(cur + 1)
        check(cur + 1, jumps - 1, path, res)
        path.pop()
    
        path.append(cur + 3)
        check(cur + 3, jumps - 1, path, res)
        path.pop()
    
        path.append(cur - 1)
        check(cur - 1, jumps - 1, path, res)
        path.pop()
    
        path.append(cur - 3)
        check(cur - 3, jumps - 1, path, res)
        path.pop()

    res = []
    check(start, length, [start], res)
    return res


result = bunny(13, 17, 2)
print(*result, sep="\n")