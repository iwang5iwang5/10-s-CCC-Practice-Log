amount=int(input())
boardstemp=input().split()
boards=[]
for n in boardstemp:
    boards.append(int(n))
boards.sort()
longest=max(boards)
def is_equal(temp,s):
    for m in range(len(temp)//2):
        if temp[0]+temp[len(temp)-1]!=s:
            return False
        else:
            temp.remove(temp[0])
            temp.remove(temp[len(temp)-1])
    return True
if amount%2==0:
    if is_equal(boards.copy(),boards[0]+boards[len(boards)-1]):
        print(len(boards)//2)
    else:
        print(1)
else:
    t=boards.copy()
    t.remove(longest)
    if is_equal(t,longest):
        print(len(t)//2)
    else:
        print(1)