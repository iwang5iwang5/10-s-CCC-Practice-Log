np=[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
fav=int(input())
played=int(input())
points=[0,0,0,0]
for n in range(played):
    cur=input().split()
    np.remove([int(cur[0]),int(cur[1])])
    if int(cur[2])>int(cur[3]):
        points[int(cur[0])-1]+=3
    elif int(cur[2]) < int(cur[3]):
        points[int(cur[1])-1] += 3
    else:
        points[int(cur[0]) - 1] += 1
        points[int(cur[1]) - 1] += 1
