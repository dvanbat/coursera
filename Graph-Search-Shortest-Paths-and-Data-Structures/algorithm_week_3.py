import heapq

def main():
    origin_array = list()
    median = list()
    with open('median.txt', 'r') as f:
        for line in f:
            origin_array.append(int(line))

    for i in range(len(origin_array)):
        heap = origin_array[:i+1]
        heap = heapq.nsmallest(i+1,origin_array[:i+1])
        l = len(heap)

        if l // 2 == 0:
            median.append(heap[int(l/2-1)])
        else:
            median.append(heap[int((l+1)/2-1)])
            
    print(sum(median) % 10000)

if __name__ == '__main__':
    main()