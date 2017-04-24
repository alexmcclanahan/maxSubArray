# divide and conquer
def findmid(a):
    if len(a)%2!=0:
        mid = (len(a)/2)-(1/2)
    if len(a)%2==0:
        mid = (len(a)/2)-1
    return mid

def findmax(a):
    mid = findmid(a)
    print mid
    leftmax = -10000
    sum=0
    lefti=0
    for i in range(mid, -1, -1):
        sum += a[i]
        if leftmax<sum:
            leftmax=sum
            lefti=i
    rightmax=-10000
    sumr=0
    righti=10
    for j in range(mid+1, len(a)):
        sumr+=a[j]
        if rightmax<sumr:
            rightmax=sumr
            righti=j
    maxXsubarray = rightmax+leftmax
    print maxXsubarray
    print [lefti,righti]
def fxn(a):
    findmax(a)


a = [-5, 1, 3, 7, -6, 16, 18, -800, 19, -500]
fxn(a)
