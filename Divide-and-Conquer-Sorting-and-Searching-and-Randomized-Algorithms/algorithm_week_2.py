f = open("count_inversion_IntegerArray.txt", "r")
arr = []
for line in f:
    arr.append(int(line))
f.close()
# print(arr)

# arr = [8,7,6,5,4,3,2,1]
# arr =[37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
new_arr = [0] * len(arr)
correct_arr = [0] * len(arr)
inc_cnt = 0

def _LocalSort (la_arr, x, y, mid_n):
    global inc_cnt
    i = 0
    j = 0
    arr1 = la_arr[x :  (x + mid_n)]
    arr2 = la_arr[x + mid_n : y + 1]
    while i < len(arr1) and j <  len(arr2):
        if arr1[i] < arr2[j] :
            new_arr [x + i + j] = arr1[i]
            i += 1
        else:
            new_arr[x + i + j] = arr2[j]
            inc_cnt += len(arr1)-i
            j += 1
    while i < len(arr1):
        new_arr [x + i + j] = arr1[i]
        i += 1
    while j < len(arr2):
        new_arr [x + i + j] = arr2[j]
        j += 1


def MergeSort1 (a_arr, x, y, arr_len):
    global inc_cnt
    if arr_len > 2:
        n = arr_len // 2
        MergeSort1(a_arr, x,  (x + n) - 1, n)
        MergeSort1(a_arr, x + n, y, (y - x - n) + 1)
        _LocalSort(new_arr, x, y, n)
    elif arr_len == 1:
        new_arr[x] = a_arr[x]
    elif arr_len == 2:
        if arr[x] > arr[y]:
            new_arr[x] = a_arr[y]
            new_arr[y] = a_arr[x]
            inc_cnt += 1
        else:
            new_arr[x] = a_arr[x]
            new_arr[y] = a_arr[y]

MergeSort1(arr, 0, len(arr) - 1, len(arr))
print(inc_cnt)