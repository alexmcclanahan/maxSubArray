def kadane(a):
    cMax=0
    max=0
    for i in range(0, len(a)):
        cMax+=a[i]
        if cMax<0:
            cMax=0
        if max<cMax:
            max=cMax
    print max
a = [-500, 1, 23, -9, 6000, 30, -522, 60, -76, 29, 19, 14, -20, -59 -900, 13, -15, 518, -18, 90]
kadane(a)
