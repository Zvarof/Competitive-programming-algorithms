### MAX or MIN Continuous sub array
## Goal : Calculate the minimal sum constitued by any number of adjacents elements of a given array. 
## Principle : Finding the first element that it is benefical to include
# Time complexity : (O)n where n is the length of the list

def find_min_sub_sum(num_array):
    if not num_array: return None                       # Check if the array/list is empty

    best_min = num_array[0]
    current_min_including_element = num_array[0]

    ## Checking for each element of the array wether it is beneficial 
    # to include the precedent sub-sum (<0) or not (>0).
    for i in range(1, len(num_array)):
        # We found the local minimum including the element
        if current_min_including_element > 0:
            current_min_including_element = num_array[i]
        # If not, the new sum is lower when including the preceding sub-sum 
        # (equivalent to the preceding sub-sum is < 0):
        else:
            current_min_including_element += num_array[i]
        # Store the 'best' min value at each iteration
        best_min = min(best_min, current_min_including_element)
    print('best_min :', best_min)
    return(best_min)


def find_max_sub_sum(num_array):
    if not num_array: return None                       # Check if the array/list is empty

    best_max = num_array[0]
    current_max_including_element = num_array[0]

    ## Checking for each element of the array wether it is beneficial 
    # to include the precedent sub-sum (<0) or not (>0).
    for i in range(1, len(num_array)):
        # We found the local maximum including the element
        if current_max_including_element < 0:
            current_max_including_element = num_array[i]
        # If not, the new sum is higher when including the preceding sub-sum 
        # (equivalent to the preceding sub-sum > 0): 
        else:
            current_max_including_element += num_array[i]
        # Store the 'best' max value at each iteration
        best_max = max(best_max, current_max_including_element)
    print('best_max :', best_max)
    return(best_max)


### Continuous Sub array sum to target
## Goal : Find the number of continuous sub array that sum exactly to the target
''' Concept : Calculer toutes les subsums ('prefix_sum') en partant du premier élèment. 
A chaque nouvelle subsums généré, checker si cette nouvelle subsum (prev_sum) 
est égale à une subsum précédente + k. 
Si oui, la subarray constitué des élèments [prev_sum+1 : élément actuel] 
(inclus) constitue une solution. 
'''

def subarraySum(nums, k):
    # Initialize a dictionary to store the prefix sum frequencies
    prefix_sum_counts = {0: 1}      # Initialize with 0 prefix sum seen once
    prefix_sum = 0                  # Initialize the cumulative sum
    count = 0                       # Initialize the count of subarrays with the target sum

    for num in nums:
        prefix_sum += num           # Calculate the cumulative sum
        # Check if prefix_sum - k exists in the dictionary's keys
        if (prefix_sum - k) in prefix_sum_counts:
            count += prefix_sum_counts[prefix_sum - k]

        # Increment the count of current prefix sum
        if prefix_sum in prefix_sum_counts:
            prefix_sum_counts[prefix_sum] += 1
        else:
            prefix_sum_counts[prefix_sum] = 1

    return count


### Combination sum to target - Multiple use of elem in array authorized
## Goal : Find the number of combinations that sum exactly to the target
# Time complexity : O(n*k*m) where k is the target and m the number of combinations
''' Concept : Storing all possible way to reach numbers from 0 to target (1 [] for each)
including the current num we iterate through + previous found sum. 
Solutions is given by the k [] 
'''
def combinationSum(nums, k):
    dp = [[] for _ in range(k+1)]

    for num in nums:
        for i in range(1, k+1):         # First column always equal to [0]
            if i<num : continue         # List remains empty
            if i==num:                  # We add num to the i[]
                dp[i].append([num])     
            else:                       # We add all previous results of i-num[]
                for prevSol in dp[i-num]:
                    dp[i].append(prevSol + [num])
     return dp[k]
    
    '''Only returning the number of solutions'''
    # return len(dp[k])     ''' Only returning the number of solutions '''

    '''Only returning unique solutions'''
    #unique_results = list(set(tuple(comb) for comb in dp[k])) '
    #return unique_results
'''
NOte : Accept negative number and produce unique solutions (considering the order)
If duplicate, each number is considered as a unique eleme (redondant solution)
'''
