import sys
input = sys.stdin.readline
j=int(input().strip('\n'))#amount of jerseys
p=int(input().strip('\n'))#number of players
list1=[]
list2=[]#request size
ans=0
for q in range(j):
    cur=input().strip('\n')
    if cur=='S':
     list1.append(1)
    if cur=='M':
     list1.append(2)
    if cur=='L':
     list1.append(3)
for q in range(p):
    cur=input().split()
    cursize = 0
    if cur[0]=='S':
        cursize = 1
    if cur[0]=='M':
        cursize = 2
    if cur[0]=='L':
        cursize = 3
    if cursize<=list1[int(cur[1])-1]:
       ans+=1
       list1[int(cur[1]) - 1] = -1
print(ans)