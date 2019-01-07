def is_square(x):
    if x == 1:
        return True
    low = 0
    high = x // 2
    root = high
    while root * root != x:
        root = (low + high) // 2
        if low + 1 >= high:
            return False
        if root * root > x:
            high = root
        else:
            low = root
    return True


numbers = [int(num) for num in input().split(' ') if is_square(int(num))]
numbers.sort(reverse=True)
print(" ".join(map(str, numbers)))
