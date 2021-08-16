dp=[]
n=int(input())
k=int(input())
def pi(nl,kl,minnum):
    if dp[nl][kl][minnum]==0:
        if nl==kl:
            dp[nl][kl][minnum]=1
        elif kl==1:
            dp[nl][kl][minnum]=1
        else:
            t=0
            for i in range(minnum,(nl//kl)+1):
                t= t+pi(nl-i,kl-1,i)
            dp[nl][kl][minnum] = t
    return dp[nl][kl][minnum]

for i in range(n+1):
    x=[]
    for j in range(k+1):
        t=[]
        for kk in range(n+1):
            t.append(0)
        x.append(x)
    dp.append(x)
print(pi(n,k,1))