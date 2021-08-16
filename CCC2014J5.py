def find():
    m=int(input())
    list1=input().split()
    list2=input().split()
    if len(list1)!=len(list2):
        return 'bad'
    for n in range(len(list1)//2):
        a=[list1[n],list2[n]]
        b=[list2[m-n-1],list1[m-n-1]]
        if a!=b:
            return 'bad'
        elif [list1[n]==list2[n]]:
            return 'bad'
    return 'good'
print(find())