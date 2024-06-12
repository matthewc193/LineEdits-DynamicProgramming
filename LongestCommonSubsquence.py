def lcs(s1, s2):
    table = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1] == s2[i-1]:
                table[i][j] = table[i-1][j-1] +1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    res = ''
    n = len(s2)
    m = len(s1)
    while n != 0 and m != 0:
        if s1[m-1] == s2[n-1]:
            res += s1[m-1]
            m -= 1
            n -= 1
        else:
            if table[n-1][m] > table[n][m-1]:
                n -= 1
            else:
                m -= 1
    return res[::-1]