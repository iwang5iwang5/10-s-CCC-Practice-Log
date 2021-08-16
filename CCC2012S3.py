list1=[0]*1001
list2=[0]*1001
N=int(input())
for i in range(N):
    a=int(input())
    list1[a]+=1
    list2[a]+=1
list2.sort()
f1=list2[1000]
f2=0
si=999
while si>=1:
    f2=list2[si]
    if list2[si]<f1:
        break
    si-=1

list3=[]
list4=[]
for i in range(1001):
    if list1[i]==f1:
        if