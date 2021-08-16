d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
ss=input()
t1=1001
t2=0
t=0
for i in range(1,len(ss),2):
    if d[ss[i]]>t1:
        t-=t2
    else:
        t+=t2
    t1=d[ss[i]]
    t2=int(ss[i-1])*d[ss[i]]
t+=t2
print(t)