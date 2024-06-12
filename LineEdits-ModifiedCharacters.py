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
            line1, line2 = line_lcs(s1[n-1], s2[m-1])
            res.append(('S', line1, line2))
            n -= 1
            m -= 1
        elif table[n-1][m] <= table[n][m-1]:
            res.append(('D', s1[n-1],''))
            n -= 1
        else:
            res.append(('I', '', s2[m-1]))
            m -= 1
    return res[::-1]

def line_back_trace(table, line1, line2):
    n = len(line1)
    m = len(line2)
    lcs = ''
    while n != 0 and m != 0:
        if line1[n-1] == line2[m-1]:
            lcs += line1[n-1]
            n -= 1
            m -= 1
        else:
            if table[n-1][m] <= table[n][m-1]:
                n -= 1
            else:
                m -= 1
    lcs = list(lcs[::-1])
    return extra_chars(list(line1), list(lcs)), extra_chars(list(line2), list(lcs))

def extra_chars(line, lcs):
    for char in range(len(line)):
        if lcs and lcs[0] == line[char]:
            lcs.pop(0)
        else:
            line[char] = '[[' + line[char] + ']]'
    line = ''.join(line)
    return line

def line_lcs(line1, line2):
    table = [[0]*(len(line2)+1) for _ in range(len(line1)+1)]
    for i in range(len(line1)+1):
        for j in range(len(line2)+1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif line1[i-1] == line2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j-1], table[i][j-1], table[i-1][j])
    return line_back_trace(table, line1, line2)
    



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

	
