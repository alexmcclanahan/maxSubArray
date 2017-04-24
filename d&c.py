# doing max subarray problem with divide and conquer...
import math

def findmid(arr):
    mid = 0
    if len(arr)%2 == 0:
        mid = int(len(arr) - 1)
    if len(arr)%2 != 0:
        y = math.floor(len(arr)/2) - 0.5
        mid = int(y)
    return mid
# variable mid is can now be used as an index for the array to denote the middle
def initialize(arr):
    low = 0
    mid = findmid(arr)
    high = int(len(arr) - 1)
    return low, mid, high
low = 0
def findmaxXsubarray(arr, low, mid, high):
    leftsum = -100000
    sum = 0
    maxleft = 0
    for i in range(mid, -1, -1):
        sum = sum + arr[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -100000
    sum = 0
    rightmax = 0
    for j in range(mid+1, high+1):
        sum = sum + arr[j]
        if sum > rightsum:
            rightsum = sum
            rightmax = j
    print (maxleft, rightmax, leftsum+rightsum)

def fxn(arr):
    findmid(arr)
    low, mid, high = initialize(arr)
    findmaxXsubarray(arr, low, mid, high)
arr = [13, 3, -25, 20, -3, 16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
fxn(arr)
