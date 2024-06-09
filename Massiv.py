def find_separation_index(arr):
    separation_index = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        elif arr[i] == 1:
            separation_index = i
            break

    return separation_index

arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
result = find_separation_index(arr)
print("Индекс разделения:", result)
