n=int(input())
ans=[]
correct=[]
m=0
for i in range(n):
    ans.append(input())
for i in range(n):
    correct.append(input())
for i in range(n):
    if ans[i]==correct[i]:
        m+=1
print(m)