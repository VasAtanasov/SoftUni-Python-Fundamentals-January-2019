def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


numbers = [int(num) for num in input().split(' ')]
bubble_sort(numbers)
print(" ".join(map(str, numbers)))
