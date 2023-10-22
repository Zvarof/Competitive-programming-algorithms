### INSERTION Sorting Algorithm
''''Principle : Iterating through each element of the array, and swapping position 
with each preceding items until at the right position'''
# Time complexity : O(n^2)

## NUMBERS or WORDS - Simple method (needs to store 3 value for swapping)
def insertion_sort_ascending(num_list):
    sorted_num_list = num_list.copy()                     # Optionnal. Good practice to not modify the original array
    for i in range(1, len(sorted_num_list)):              # Last non-listed element in the list
        for j in range(i, 0, -1):                         # Iterating through previously listed element, and swapping if necessary
            if sorted_num_list[j] < sorted_num_list[j-1]:
                sorted_num_list[j], sorted_num_list[j-1] = sorted_num_list[j-1], sorted_num_list[j]
            else:
                break                                     # No need to continue further are all element are already sorted
    return sorted_num_list

def insertion_sort_num_descending(num_list):
    sorted_num_list = num_list.copy()                     
    for i in range(1, len(sorted_num_list)):                     
        for j in range(i, 0, -1):                         
            if sorted_num_list[j] > sorted_num_list[j-1]:
                sorted_num_list[j], sorted_num_list[j-1] = sorted_num_list[j-1], sorted_num_list[j]
            else:
                break                                     
    return sorted_num_list

''' For sorting letter in a word just replace 'sorted_num_list = num_list.copy()' 
by sorted_word = list(word) and 'return sorted_num_list' by 'return ''.join(sorted_word)' 
'''

## NUMBERS or WORDS - Optimized method 
''' Needs to store 1 value for switching + 1 comparaison instead of 3 operations '''
def insertion_sort_ascending(num_list):
    sorted_num_list = num_list.copy()      
    for i in range(1, len(sorted_num_list)):
        curNum = sorted_num_list[i]
        for j in range(i, 0, -1):                         
            if sorted_num_list[j-1] > curNum:
                sorted_num_list[j] = sorted_num_list[j-1]
                if j == 1:
                   sorted_num_list[0] = curNum
            else:
                sorted_num_list[j] = curNum
                break
    return sorted_num_list


### SWAP Sorting Algorithm
''''Principle : Iterating through the list, search for the min non-sorted element.
Then swap the min at the first non-sorted position'''
# Time complexity : O(n^2)
def selection_sort_ascending(num_list):
    for i in range (0, len(num_list) -1):
        minIndex = i
        for j in range (i+1, len(num_list)):
            if num_list[j] < num_list[minIndex]:
                minIndex = j
        if minIndex != i:
            num_list[i], num_list[minIndex] = num_list[minIndex], num_list[i]
    return num_list


### BUBBLE Sorting Algorithm
'''' Iterating through the list and swapping by pair of adjacents elements.
The last non-sorted element must be the biggest and we do not need to iterate through it anymore '''
# Time complexity : O(n^2)

def bublle_sort_ascending(num_list):
    for i in range (0, len(num_list) -1):
        for j in range (0, len(num_list)-1 -i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


### MERGE Sorting Algorithm
'''Recursive solution through sorting pair of sub-list to create greater sublist
until reaching the original unsorted list.
Interesting for large dataset '''
# Time complexity : O(n*log n)

def merge_sort(num_list):
    def merge_sort2(num_list, first, last):
        if first < last:
            middle = (first + last)//2
            merge_sort2(num_list, first, middle)        ## Sub the problem until having a list of 1 element (Left part)
            merge_sort2(num_list, middle+1, last)       ## Sub the problem until having a list of 1 element (Right part)
            merge(num_list, first, middle, last)        ## Executed when both side of merge2 have reach base case
    
    def merge(num_list, first, middle, last):
        Left = num_list[first:middle]
        Right = num_list[middle:last+1]
        Left.append(9999999999)                        ## Similar to inf, making sure to not run out of index
        Right.append(9999999999)                       ## Similar to inf, making sure to not run out of index
        i = j = 0
        for k in range(first, last+1):
            if Left[i] <= Right[j]:
                num_list[k] = Left[i]
                i += 1
            else:
                num_list[k] = Right[j]
                j += 1

    merge_sort2(num_list, 0, len(num_list)-1)
    return num_list


### Quick Sorting Algorithm
''' Using a 'Pivot' for comparaison with other elements
If the elem is < Pivot : It take the position next to the pivot
and moove the 'Border' by 1 position to the right.
Recursive solution applied to both side of the new pivot's position'
'''
# Time complexity : Worst case : O(n^2) | Average O(n*log n)

def quick_sort(num_list):

    def quick_sort2(num_list, low, hi):
        if low < hi:                                 # More than 1 item to be sorted
            p = partition(num_list, low, hi)
            quick_sort2(num_list, low, p-1)
            quick_sort2(num_list, p+1, hi)

    def get_pivot(num_list, low, hi):
        # Get the median value from low, mid, hi for the pivot
        mid = (hi + low) //2
        pivot = hi
        if num_list[low] < num_list[mid]:
            if num_list[mid] < num_list[hi]:
                pivot = mid
        elif num_list[low] < num_list[hi]:
            pivot = low
        return pivot
    
    def partition(num_list, low, hi):
        pivotIndex = get_pivot(num_list, low, hi)
        pivotValue = num_list[pivotIndex]
        num_list[pivotIndex], num_list[low] = num_list[low], num_list[pivotIndex]       # Put the pivot at the most left position
        border = low                                                                    # Start the border at the most left position

        for i in range(low, hi+1):
            if num_list[i] < pivotValue:
                border += 1
                num_list[i], num_list[border] = num_list[border], num_list[i]   # Put the value to the right of the old border
        # Replace the last border with the pivot value (all value to the left are < to the pivot)
        num_list[low], num_list[border] = num_list[border], num_list[low]

        return border
    
    quick_sort2(num_list, 0, len(num_list)-1)
    return num_list

''' Can be further optimize by combining it with different sorting methode when
the length becomes lower than a certain number '''

''' Python built-in sort is much much faster and run an optimized combinations of 
these differents methods + implemented in C (most of the difference ?)'''