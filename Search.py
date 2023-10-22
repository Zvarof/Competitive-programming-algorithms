### List - Binary search 
## Condition : The array is already sorted

'''
Concept : Initialize the 'middle value' as the average or the first and last element.
Comparing whether the searched value is greater, equal or lower to the middle. 
-> Allow elimination of half the non-test population. 
Actualise the first or last and recalculate the middle and repeat.
'''

def FindIndex(num_list, target):
    left = 0
    right = len(num_list)-1

    while right >= left:
        middle = (left+right) // 2
        if num_list[middle] < target:
            left = middle + 1
        elif num_list[middle] > target:
            right = middle - 1
        else:
            return middle

    return 'Target not found'

### Tree - General Tree or Unsorted Binary Tree - Depth first  

def findNodeInGeneralTree(root, target):
    if root.value == target:
        return 'The node IS in the tree'
    for children in root.children:
        result = findNodeInGeneralTree(children, target)
        if result == 'The node IS in the tree':
            return result
    return 'The node is NOT in the tree'

### Tree - Binary Search Tree - Depth first 
    



