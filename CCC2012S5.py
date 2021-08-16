init=input().split()
R=int(init[0])
C=int(init[1])
dp=[]
for i in range(R):
    dp.append([1]*C)

cats=int(input())
for i in range(cats):
    init=input().split()
    dp[int(init[0])-1][int(init[1])-1]=0

for i in range(R):
    for j in range(C):
        if dp[i][j]!=0 and not (i==0 and j==0):
            if i==0:
                dp[i][j] = dp[i][j - 1]
            elif j==0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[R-1][C-1])