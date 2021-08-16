import sys
input = sys.stdin.readline

def binarySearch(arr, l, r, x):
    if r > l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            del arr[mid]
            return mid
        elif arr[mid] > x:
            if mid-1 >= 0 and x > arr[mid-1]:
                del arr[mid-1]
                return mid-1
            return binarySearch(arr, l, mid - 1, x)

        else:
            if mid+1 < len(arr) and x < arr[mid+1]:
                del arr[mid]
                return mid
            if mid + 1 < len(arr) and x == arr[mid + 1]:
                del arr[mid+1]
                return mid+1
            return binarySearch(arr, mid + 1, r, x)
    else:
        if l == r and arr[r] <= x:
            del arr[r]
            return r
        return -1


ans=0
gates=int(input().strip('\n'))
planes=int(input().strip('\n'))
list0=[]
taken=[]
for n in range(planes):
    list0.append(int(input().strip('\n')))
for n in range(gates):
    taken.append(n+1)
for n in list0:
    cur=binarySearch(taken, 0, len(taken)-1, n)
    if cur==-1:
        break
    ans += 1
print(ans)