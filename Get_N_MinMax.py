''' List of most efficient programs to get N greatest or lowest element from an array
Options : 
    0. Min() / Max ()
    1. sort[indexing]
    2. heapq
When to choose 1 over the other : 
    For retrieving a single value 
        use -- min() or max()
    For retrieving a small portion of element (or if insertions/operations will latter be down on the array, while you still need to maintain order)
        use -- heapq
    For retrieving a large portion of elements use -- sort[indexing]
        use -- sort[indexing]
'''

# heap options :
import heapq

def find_n_greatest_numbers(arr, n):
    # Convert the input list to a min-heap with the first N elements
    min_heap = arr[:n]
    heapq.heapify(min_heap)
    
    # Iterate through the remaining elements in the list
    for num in arr[n:]:
        # If the current element is greater than the smallest element in the min-heap
        if num > min_heap[0]:
            # Replace the smallest element with the current element
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    # The min-heap now contains the N greatest numbers
    return sorted(min_heap, reverse=True)


import heapq

def find_n_lowest_numbers(arr, n):
    # Convert the input list to a min-heap with the first N elements
    min_heap = heapq.heapify(arr)
    
    # Replace the smallest element with the current element
    solution = []
    for _ in range (n):
        solution.append(heapq.heappop(min_heap))
    return solution

''' 
Or alternatively use : heap.nlargest(N, num_list) | heap.nsmallest(N, num_list)
'''
