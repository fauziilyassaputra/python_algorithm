import heapq

# Min-heap

min_heap = []
heapq.heappush(min_heap, 43)
heapq.heappush(min_heap, 12)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 76)
heapq.heappush(min_heap, 21)
heapq.heappush(min_heap, 54)
heapq.heappush(min_heap, 67)

# menampilkan isi min-heap
print("Min-heap: ", min_heap)
# Min-heap:  [7, 21, 12, 76, 43, 54, 67]

# mengeluarkan nilai terkecil
print("pop :",  heapq.heappop(min_heap))
# Pop : 7


#Max-heap

max_heap = []
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -7)

# meanmpilkan isi max-heap
print("max-heap: ", max_heap)

#mengeluarkan nilai terbesar
print("pop :", -heapq.heappop(max_heap))
