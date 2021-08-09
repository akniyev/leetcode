arr = [1, 2, 3]
n = len(arr)
shift = 1
arr = arr[shift:] + arr[:shift]

i = 0
j = n - 1

if arr[i] < arr[j]:
    print("There is no shift")
else:
    i += 1
    while i < j:
        m = (i + j) // 2
        if arr[m] < arr[m - 1]:
            break
        elif arr[m] > arr[0]:
            i = m + 1
        elif arr[m] < arr[0]:
            j = m - 1
        else:
            print("Something went wrong!")

    m = (i + j) // 2
    print(m)

print(arr)