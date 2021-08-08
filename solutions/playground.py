def binary_search(value, arr, start_index):
    n = len(arr)
    i = start_index
    j = n - 1

    m = 0
    while i < j:
        m = (i + j) // 2
        if arr[m] == value:
            return m
        elif arr[m] < value:
            i = m + 1
        else:
            j = m - 1

    while m > 0 and arr[m] > value:
        m -= 1

    return m


def find_duplicates(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    if n > m:
        n, m = m, n
        arr1, arr2 = arr2, arr1

    if n == 0 or m == 0:
        return []

    result = []

    j0 = 0

    for i in range(n):
        j = binary_search(arr1[i], arr2, j0)
        if arr2[j] == arr1[i]:
            result.append(arr1[i])
        j0 = j

    return result

find_duplicates([1,2,3,5,6,7], [3,6,7,8,20])