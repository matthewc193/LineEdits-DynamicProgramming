def back_trace(table,s1,s2):
    res = []
    m = len(s2)
    n = len(s1)
    while n != 0 or m != 0:
        if n == 0 or m == 0:
            if n == 0 and m == 0:
                return res
            if n == 0:
                res.append(('I', '', s2[m-1])) 
                m -= 1
            elif m == 0:
                res.append(('D',s1[n-1], ''))
                n -= 1
        elif s2[m-1] == s1[n-1]:
            res.append(('C',s1[n-1], s2[m-1]))
            n -= 1
            m -= 1
        elif table[n-1][m-1] <= table[n-1][m] and table[n-1][m-1] <= table[n][m-1]:
            res.append(('S', s1[n-1], s2[m-1]))
            n -= 1
            m -= 1
        elif table[n-1][m] <= table[n][m-1]:
            res.append(('D', s1[n-1],''))
            n -= 1
        else:
            res.append(('I', '', s2[m-1]))
            m -= 1
    return res[::-1]

def line_edits(s1, s2):
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    table = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i-1][j-1], table[i][j-1], table[i-1][j]) + 1
    return back_trace(table,s1,s2)

	


