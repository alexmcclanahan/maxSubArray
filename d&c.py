def midIndex(a):
    # fxn to find midpoint of array
    low = 0
    high = len(a)
    return int((high-low)/2)
a = [-5, 10, -1, 15, 25, 13, -10]


def maxX(a, low, mid, high):
    mid = midIndex(a)
    sumL = -float('inf')
    leftind = 0
    tempL = 0
    for i in range(mid, -1, -1):
        tempL += a[i]
        if tempL > sumL:
            sumL = tempL
            leftind = i

    sumR = -float('inf')
    rightind = 0
    tempR = 0
    for j in range(mid+1, len(a)):
        tempR += a[j]
        if tempR > sumR:
            sumR = tempR
            rightind = j

    sum = sumR + sumL
    return leftind, rightind, sum

def recursion(a, low, high):
    if high - 1 == low:
        return low, high, a[low]
    else:
        midd = int((high - low)/2)
        left_low, left_high, left_sum = recursion(a, low, midd)
        right_low, right_high, right_sum = recursion(a, midd + 1, high)
        cross_low, cross_high, cross_sum = maxX(a, low, midd, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        elif cross_sum > left_sum and cross_sum > right_sum:
            return cross_low, cross_high, cross_sum

recursion(a, 0, len(a))
