list1 = []


def setrow(row):
    if list1[row][0] != 'X' and list1[row][1] != 'X' and list1[row][2] == 'X':
        list1[row][2] = 2*list1[row][1] - list1[row][0];
        return
    if list1[row][0] != 'X' and list1[row][2] != 'X' and list1[row][1] == 'X':
        list1[row][1] = int((list1[row][2] + list1[row][0])/2)
        return
    if list1[row][2] != 'X' and list1[row][1] != 'X' and list1[row][0] == 'X':
        list1[row][0] = 2*list1[row][1] - list1[row][2]
        return


def setcol(col):
    if list1[0][col] != 'X' and list1[1][col] != 'X' and list1[2][col] == 'X':
        list1[2][col] = 2*list1[1][col] - list1[0][col];
        return
    if list1[0][col] != 'X' and list1[2][col] != 'X' and list1[1][col] == 'X':
        list1[1][col] = int((list1[2][col] + list1[0][col])/2)
        return
    if list1[2][col] != 'X' and list1[1][col] != 'X' and list1[0][col] == 'X':
        list1[0][col] = 2*list1[1][col] - list1[2][col]
        return


def setonerow(row, col, d):# set a row with interval=d
    if col == 0:
        list1[row][1] = list1[row][0] + d
        list1[row][2] = list1[row][1] + d
        return
    if col == 1:
        list1[row][0] = list1[row][1] - d
        list1[row][2] = list1[row][1] + d
        return
    if col == 2:
        list1[row][1] = list1[row][2] - d
        list1[row][0] = list1[row][1] - d
        return


def setelement(row, d): #set all rows with the interval=d
    for i in range(3):
        if i == row:
            continue
        j = 0
        while j < 3:
            if list1[i][j] != 'X':
                break
            j += 1
        if j == 0:
            list1[i][1] = list1[i][0] + d
            list1[i][2] = list1[i][1] + d
        elif j == 1:
            list1[i][2] = list1[i][1] + d
            list1[i][0] = list1[i][1] - d
        else:
            list1[i][1] = list1[i][2] - d
            list1[i][0] = list1[i][1] - d


def printmatrix(): #print the answer
    print(list1[0][0], list1[0][1], list1[0][2])
    print(list1[1][0], list1[1][1], list1[1][2])
    print(list1[2][0], list1[2][1], list1[2][2])


def getx(): #find the amount of X in the square
    n = 0
    for i in range(3):
        for j in range(3):
            if list1[i][j] == 'X':
                n += 1
    return n


def handlefour():
    for row in range(3):
        setrow(row)
    for col in range(3):
        setcol(col)
    if getx() == 4:
        d = 0
        i = 0
        while i < 3:
            if list1[i][0] != 'X' and list1[i][1] != 'X' and list1[i][2] != 'X':
                d = list1[i][1] - list1[i][0]
                break
            i += 1
        setelement(i, d)


def handlefive():
    handlefour()
    if getx() == 4:
        d = 0
        i = 0
        while i < 3:
            if list1[i][0] != 'X' and list1[i][1] != 'X' and list1[i][2] != 'X':
                break
            i += 1
        setelement(i, d)


def handlesix():
    for q in range(3):
        setrow(q)
    for p in range(3):
        setcol(p)
    if getx() == 6:
        if list1[1][1] == 'X':
            if list1[0][1] != 'X':
                list1[1][1] = list1[0][1]
            elif list1[1][0] != 'X':
                list1[1][1] = list1[1][0]
            elif list1[1][2] != 'X':
                list1[1][1] = list1[1][2]
            else:
                list1[1][1] == list1[2][1]
        else:
            list1[1][0] = list1[1][1]


def handleseven():
    for q in range(3):
        setrow(q)
    for p in range(3):
        setcol(p)
    if getx() == 7:
        ct = 0
        sx = 0
        sy = 0
        ex = 0
        ey = 0
        for m in range(3):
            for n in range(3):
                if list1[m][n] != 'X':
                    if ct == 0:
                        sx = m
                        sy = n
                        ct += 1
                    else:
                        ex = m
                        ey = n
                        ct += 1
                if ct == 2:
                    break
            if ct == 2:
                break

        diff = list1[ex][ey] - list1[sx][sy]
        xsteps = abs(ex - sx)
        ysteps = abs(ey - sy)
        if xsteps == ysteps:
            setonerow(sx, sy, 0)
            setonerow(ex, ey, 0)
        else:
            if ysteps % 2 != 0:
                if diff % 2 == 0:
                    setonerow(sx, sy, 2)
                    setonerow(ex, ey, 2)
                else:
                    setonerow(sx, sy, 1)
                    setonerow(ex, ey, 1)
            else:
                setonerow(sx, sy, 2)
                setonerow(ex, ey, 2)


def setall(aa):
    for k in range(3):
        for j in range(3):
            list1[k][j] = aa


xnum = 0
for i in range(3):
    cur = input().rstrip().split(" ")
    content = []

    for x in cur:
        if x == 'X':
            content.append(x)
            xnum += 1
        else:
            content.append(int(x))
    list1.append(content)

while xnum > 0:
    if xnum < 5:
        handlefour()
    elif xnum == 5:
        handlefive()
    elif xnum == 6:
        handlesix()
    elif xnum == 7:
        handleseven()
    elif xnum == 8:
        for a in range(3):
            c = False
            for b in range(3):
                if list1[a][b] != 'X':
                    setall(list1[a][b])
                    c = True
                    break

            if c:
                break
    else:
        setall(0)

    xnum = getx()

printmatrix()