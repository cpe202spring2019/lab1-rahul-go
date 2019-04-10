
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError

    maximum = int_list[0]
    for i in int_list:
        if i > maximum:
            maximum = i
    return maximum



def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if len(int_list) == 1:
        return int_list

    return [int_list[-1]] + reverse_rec(int_list[:-1])



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    
    # If list is None, raise ValueError
    if int_list == None:
        raise ValueError

    # Integer average
    mid = (low + high) // 2

    # Final check
    if mid == low:
        # Match found
        if int_list[mid] == target:
            return mid
        # Mathch found in upper edge case
        if int_list[mid+1] == target:
            return mid+1
        # Match not found
        return None

    # Match found
    if int_list[mid] == target:
        return mid
    # Value too low
    elif int_list[mid] < target:
        return bin_search(target, mid, high, int_list)
    # Value too high
    elif int_list[mid] > target:
        return bin_search(target, low, mid, int_list)