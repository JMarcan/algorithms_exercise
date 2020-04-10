def rearrange_digits(input_arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Time complexity: O(n log(n)) due to mergesort
    
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two largest possible integers created from provided numbers
    """    
    #empty arrays holding final digits
    out1 = []
    out2 = []
    
    # sort the list in ascending order
    input_arr = mergesort(input_arr)
    
    # build two largest possible integers from provided numbers
    for i, element in enumerate(reversed(input_arr)):
        if i % 2 == 0:
            out1.append(element)
        else:
            out2.append(element)
            
    # Store lists of digits as integers
    out1 = int(''.join([str(i) for i in out1]))
    out2 = int(''.join([str(i) for i in out2]))
    
    return out1, out2
    
    
    
def mergesort(input_arr):
    """
    Sort the array by application of merge sort
    
    Time complexity: O(n log(n))
    Space Complexity: O(n)
    
    Args:
       input_arr(array): Input array with numbers to be sorted
       
     Returns:
       sorted_arr(array) Sorted array with numbers in ascending order
    """ 
    if len(input_arr) <= 1:
        return input_arr
    
    mid = len(input_arr) // 2
    left = input_arr[:mid]
    right = input_arr[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return _merge(left, right)

def _merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def test_rearrange_digits(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

def test_mergesort(test_case):
    output = mergesort(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_mergesort([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
test_mergesort([[4, 6, 2, 5, 9, 8], [2, 4, 5, 6, 8, 9]])

test_rearrange_digits([[1, 2, 3, 4, 5], [542, 31]])
test_rearrange_digits([[4, 6, 2, 5, 9, 8], [964, 852]])