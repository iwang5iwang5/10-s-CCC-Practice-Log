def compute():
    term=int(input())
    list=str.split(input())
    for n in range(len(list)):
        list[n]=int(list[n])
    list.sort()
    if term%2==0:
        pivot=term//2
    else:
        pivot=term//2+1
    left=list[:pivot]
    right=list[pivot:]
    #print(left,right)
    for n in range(len(left)):
        print(left[len(left)-n-1],end=' ')
        if n<len(right):
         print(right[n],end=' ')

compute()
