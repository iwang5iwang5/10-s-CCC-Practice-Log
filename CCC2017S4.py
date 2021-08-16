init=input().split()
class edge:
    def __init__(self,src,dst,weight):
        self.src=src
        self.dst=dst
        self.weight=weight
def root(v,id):
    while id[v]!=v:
        id[v]=id[id[v]]
        v=id[v]
    return v
def unionadj(v1,v2,id):
    r1=root(v1,id)
    r2=root(v2,id)
    id[r2]=r1
def activeornot(activelist,src,dst):
    for x in activelist:
        if x.src==src and x.dst==dst:
            return True
    return False
N=int(init[0])
id=[]
activelist=[]
for i in range(N+1):
    id.append(i)
EN=int(init[1])
days=0
edgelist=[]

for i in range(EN):
    ss=input().split()
    src=int(ss[0])
    dst=int(ss[1])
    weight=int(ss[2])
    cur=edge(src,dst,weight)
    edgelist.append(cur)
    if i<N-1:
        activelist.append(cur)

edgelist=sorted(edgelist,key=lambda edge:edge.weight)

for x in edgelist:
    csrc=x.src
    cdst=x.dst
    cweight=x.weight
    if root(csrc,id)!=root(cdst,id):
        unionadj(csrc,cdst,id)
        if not activeornot(activelist,csrc,cdst):
            days+=1
print(days)
