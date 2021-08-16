N = int(input())
S = input().rstrip().split()
L = [0]*2001
F = [0]*4002
topfence = 0
for x in S:
    fence = int(x)
    if fence > topfence:
        topfence = fence
    L[fence] += 1

for i in range(topfence+1):
    if L[i] > 0:
        t = i + i
        num = L[i]//2
        F[t] += num
        for j in range(i+1, topfence+1, 1):
            if L[j] > 0:
                p = i+j
                np = min(L[i], L[j])
                F[p] += np

cnt = 0
maxLen = 0

for i in range(topfence*2+1):
    if F[i] > 0:
        if F[i] > maxLen:
            maxLen = F[i]
            cnt = 1
        else:
            if F[i] == maxLen:
                cnt += 1

print(maxLen, cnt)
