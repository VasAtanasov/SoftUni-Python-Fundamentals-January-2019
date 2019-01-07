numbers = [int(num) for num in input().split(' ')]


def count_odd_numbers_at_odd_indexes(collection):
    result = []
    for i in range(len(collection)):
        if i % 2 != 0 and collection[i] % 2 != 0:
            result.append(f'Index {i} -> {collection[i]}')
    return result


print('\n'.join(count_odd_numbers_at_odd_indexes(numbers)))
