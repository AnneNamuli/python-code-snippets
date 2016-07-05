def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist =  [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
bubbleSort(alist)
print(alist)
