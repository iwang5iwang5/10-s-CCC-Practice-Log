import sys
class Node:
    def __init__(self, i, j, steps):
        self.x = i  # Assign data
        self.y = j  # Initialize
        self.steps = steps
sss = input().split(" ")
N = int(sss[0])
M = int(sss[1])

data = []
route = []
visited = []
clist = []
qlist = []
sx = 0
sy = 0
def updatec(x,y):  # checks if a cell can be reached(is not a wall)
    if data[x][y] == 'W':
        return False
    if data[x][y] == '.' or data[x][y] == 'S':
        route[x][y] = -1
    return True

def handlecamera():
    for node in clist:
        x = node.x
        y = node.y
        route[x][y] = -1
        row = y+1
        while row < M:
            if updatec(x, row) == False:
                break
            row += 1
        row = y-1
        while row >= 0:
            if updatec(x, row) == False:
                break
            row -= 1
        col = x + 1
        while col < len(data):
            if updatec(col, y) == False:
                break
            col += 1
        col = y-1
        while col >= 0:
            if updatec(col, y) == False:
                break
            col -= 1


def handlecell(node, x, y):
    if route[x][y] == -1:
        return False
    if data[x][y] == '.':
        if visited[x][y] and route[x][y] <= node.steps+1:
            return False
        else:
            route[x][y] = node.steps + 1
            return True
    elif data[x][y] == 'L' or data[x][y] == 'D' or data[x][y] == 'R' or data[x][y] == 'U':
        if visited[x][y] and route[x][y] <= node.steps:
            return False
        else:
            route[x][y] = node.steps
            return True
    else:
        return False
def setqueue(node, x, y):
    if handlecell(node, x, y):
            visited[x][y] = True
            qlist.append(Node(x, y, route[x][y]))

for i in range(N):
    s = input()
    curd = []
    curr = []
    curv = []
    for j in range (M):
        curd.append(s[j])
        curr.append(sys.maxsize)
        curv.append(False)
        if s[j] == 'S':
            sx = i
            sy = j
        if s[j] == 'C':
            clist.append(Node(i, j, -1))

    data.append(curd)
    route.append(curr)
    visited.append(curv)

handlecamera()
if route[sx][sy] != -1:
    route[sx][sy] = 0
    visited[sx][sy] = True
    qlist.append(Node(sx, sy, 0))

while len(qlist) > 0:
    cur = qlist[0]
    qlist.remove(cur)
    cx = cur.x
    cy = cur.y
    if data[cx][cy] == 'L':
        setqueue(cur, cx, cy-1)
    elif data[cx][cy] == 'R':
        setqueue(cur, cx, cy+1)
    elif data[cx][cy] == 'U':
        setqueue(cur, cx-1, cy)
    elif data[cx][cy] == 'D':
        setqueue(cur, cx+1, cy)
    elif data[cx][cy] == '.' or data[cx][cy] == 'S':
        setqueue(cur, cx, cy - 1)
        setqueue(cur, cx, cy + 1)
        setqueue(cur, cx - 1, cy)
        setqueue(cur, cx + 1, cy)

for i in range(N):
    for j in range(M):
        if data[i][j] == '.':
            t = route[i][j];
            if t == sys.maxsize:
                t = -1
            print(t);
