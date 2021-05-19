f = open("quick_sort.txt", "r")
arr = []
for line in f:
    arr.append(int(line))
f.close()

# arr = [10,6,3,7,9,2,5,8,1,4]
# arr = [3,2,1,4,5]
# arr = [2,1,12,13,16,10,9,5,18,8,17,20,19,3,4,11,14,6,7,15]
arr_origin = arr.copy()
cnt = 0

def quick_sort(a_arr):
    global cnt
    if len(a_arr) <= 1:
        return a_arr
    pivot = a_arr[0]
    i = 1
    for j in range(1, len(a_arr)):
        if a_arr[j] < pivot:
            a_arr[j], a_arr[i] = a_arr[i],a_arr[j]
            i += 1
    a_arr[0],a_arr[i-1] = a_arr[i-1],a_arr[0]
    cnt += (len(a_arr) - 1)
    return quick_sort(a_arr[:i-1]) + [a_arr[i-1]] + quick_sort(a_arr[i:])

def quick_sort_back(a_arr):
    global cnt
    if len(a_arr) <= 1:
        return a_arr
    a_arr[0], a_arr[-1] = a_arr[-1],a_arr[0]
    pivot = a_arr[0]
    i = 1
    for j in range(1, len(a_arr)):
        if a_arr[j] < pivot:
            a_arr[j], a_arr[i] = a_arr[i],a_arr[j]
            i += 1
    a_arr[0],a_arr[i-1] = a_arr[i-1],a_arr[0]
    cnt += (len(a_arr) - 1)
    return quick_sort_back(a_arr[:i-1]) + [a_arr[i-1]] + quick_sort_back(a_arr[i:])

def quick_sort_median(a_arr):

    def _median(a_med, a_zip_ind):
        l_arr = a_med.copy()
        l_arr.sort()
        return a_zip_ind[a_med.index(l_arr[1])]

    global cnt

    if len(a_arr) <= 1:
        return a_arr
    if len(a_arr) % 2 == 0:
        k = int(len(a_arr) // 2 - 1)
    else:
        k = int((len(a_arr) // 2) )
    med = _median([a_arr[0],a_arr[k],a_arr[-1]], [0, k, -1])
    a_arr[0], a_arr[med] = a_arr[med],a_arr[0]
    pivot = a_arr[0]
    i = 1
    for j in range(1, len(a_arr)):
        if a_arr[j] < pivot:
            a_arr[j], a_arr[i] = a_arr[i],a_arr[j]
            i += 1
    a_arr[0],a_arr[i-1] = a_arr[i-1],a_arr[0]
    cnt += (len(a_arr) - 1)
    return quick_sort_median(a_arr[:i-1]) + [a_arr[i-1]] + quick_sort_median(a_arr[i:])

print('----------------')
l = quick_sort(arr)
print('first ', cnt)

cnt = 0
print('----------------')
arr = arr_origin.copy()
l = quick_sort_back(arr)
print('last ', cnt)

cnt = 0
print('----------------')
arr = arr_origin.copy()
l = quick_sort_median(arr)
print('median ', cnt)
print('----------------')