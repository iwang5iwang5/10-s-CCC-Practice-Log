import math
cycle=int(input())
def find_prime(n):
    for m in range(2,n):
        cur = int(math.sqrt(m))
        isprime= True
        if m % 2 == 0:
            isprime = False
        for x in range(3,cur+1,2):
            if m%x==0:
                isprime= False
        if isprime:
            prime1=m
            other=n-prime1
            cur = int(math.sqrt(other))
            bothprime = True
            if other % 2 == 0:
                bothprime = False
            for y in range(3, cur+1,2):
                if other % y == 0:
                    bothprime = False
            if bothprime:
                return prime1,other
for a in range(cycle):
 c=find_prime(int(input())*2)
 print(c[0],c[1])