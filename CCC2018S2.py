list=[[4,3,2,1],[7,5,4,2],[9,7,6,3],[13,9,7,5]]
for n in range(len(list)):
    print(list[n])
for a in range(2):
    for b in range(4):
        list[a][b],list[b][a]=list[b][a],list[a][b]
for n in range(len(list)):
    print(list[n])
if list[0][1]<list[1][1]<list[2][1] and list[0][2]<list[1][2]<list[2][2] and list[0][3]<list[1][3]<list[2][3]:
    print(list)
else:
    for a in range(2):
        for b in range(4):
            list[a][b], list[b][a] = list[b][a], list[a][b]
    for n in range(len(list)):
        print(list[n])
    if list[0][1] < list[1][1] < list[2][1] and list[0][2] < list[1][2] < list[2][2] and list[0][3] < list[1][3] < \
            list[2][3]:
        print(list)