class Node:
    def __init__(self, content, steps, x, y):
        self.visited = 0
        self.type=content
        self.steps=steps
        self.x=x
        self.y=y

def handlecamera(node, graph):
    curX=node.x
    curY=node.y
    for x in graph:
        x[curY].type="W"
    for x in graph[curX]:
        x.type="W"

def handlecell(start, dest, graph,):
    sv = start
    dv = dest
    pq=[]
    sv.steps = 0
    pq.append(sv)
    cv = pq[0]

    while len(pq) > 0:  # bellman ford's
        if cv == dv:
            break
        cv=pq.pop(0)
        cv.visited = 1

        if graph[cv.x][cv.y].type=="." or graph[cv.x][cv.y].type=="S":
            if cv.x>=1 and graph[cv.x-1][cv.y].type!="W" and (graph[cv.x-1][cv.y].visited==0 or cv.steps+1<graph[cv.x-1][cv.y].steps):
                graph[cv.x - 1][cv.y].steps=cv.steps+1
                pq.append(graph[cv.x - 1][cv.y])
            if cv.x<len(graph)-1 and graph[cv.x+1][cv.y].type!="W" and (graph[cv.x+1][cv.y].visited==0 or cv.steps+1<graph[cv.x+1][cv.y].steps):
                graph[cv.x + 1][cv.y].steps = cv.steps + 1
                pq.append(graph[cv.x + 1][cv.y])
            if cv.y>=1 and graph[cv.x][cv.y-1].type!="W" and (graph[cv.x][cv.y-1].visited==0 or cv.steps+1<graph[cv.x][cv.y-1].steps):
                graph[cv.x][cv.y-1].steps = cv.steps + 1
                pq.append(graph[cv.x][cv.y-1])
            if cv.y<len(graph[0]) and graph[cv.x][cv.y+1].type!="W" and (graph[cv.x][cv.y+1].visited==0 or cv.steps+1<graph[cv.x][cv.y+1].steps):
                graph[cv.x][cv.y+1].steps = cv.steps + 1
                pq.append(graph[cv.x][cv.y+1])


    """
        if cv.steps + 1 < graph:
            visited[cv] = 0
        if graph[cv][i] > 0 and visited[i] == 0:
            dist[i] = dist[cv] + graph[cv][i]
            if i not in pq:
                pq.append(i)

    mindis = 10000000
    for i in range(N):
        if i in pq and dist[i] < mindis:
            cv = i
            mindis = dist[i]
    """
    print(graph[dv.x][dv.y].steps)
init=input().split()
N = int(init[0])
M = int(init[1])

graph=[]
for i in range(N):
    curLine=input()
    toAdd = []
    for j in range(M):
        toAdd.append(Node(curLine[j], -1, i, j))
    graph.append(toAdd)
startX=0
startY=0
for i in graph:
    for j in i:
        if j.type=="C":
            handlecamera(j, graph)
        if j.type=="S":
            startX=j.x
            startY=j.y

for i in graph:
    for j in i:
        if j.type==".":
            handlecell(graph[startX][startY], graph[j.x][j.y], graph)

"""
5
5
WWWWW
W...W
W...W
W...W
WWWWW
"""