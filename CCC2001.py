def j3():
    money=int(input())
    one=int(input())
    two=int(input())
    three=int(input())
    played=0
    while money > 0:
        if money>0:
            money-=1
            one+=1
            if one==35:
                one=0
                money+=30
            played+=1
        if money>0:
            money-=1
            two+=1
            if two==100:
                two=0
                money+=60
            played += 1
        if money>0:
            money-=1
            three+=1
            if three==10:
                three=0
                money+=9
            played += 1
    return played
print(j3())

def j4():
    start=int(input())
    streams={}
    for n in range(start):
        streams[n]=(int(input()))
    i=0
    while i!=77:
        i = int(input())
        if i==99:
            temp=int(input())
            sp=int(input())//100
            streams[temp]=streams[temp]*sp


