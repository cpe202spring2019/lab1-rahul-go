# RAHUL GOYAL
# CPE 202-03
# April 10, 2019

def max_list_iter(int_list):  # must use iteration not recursion
    """Finds the max of a list of numbers and returns the value (not the index).
    If int_list is empty, returns None. If list is None, raises ValueError."""
    if int_list == None:
        raise ValueError
    if int_list == []:
        return None

    maximum = int_list[0]
    for i in int_list:
        if i > maximum:
            maximum = i
    return maximum



def reverse_rec(int_list):   # must use recursion
    """Recursively reverses a list of numbers and returns the reversed list.
    If list is None, raises ValueError."""

    # If list is None, raise ValueError
    if int_list == None:
        raise ValueError

    # Check if list empty or last item
    if int_list == []:
        return int_list

    return [int_list[-1]] + reverse_rec(int_list[:-1])



def bin_search(target, low, high, int_list):  # must use recursion
    """Searches for target in int_list[low...high] and returns index if found.
    If target is not found returns None. If list is None, raises ValueError."""

    # If list is None, raise ValueError
    if int_list == None:
        raise ValueError

    # If list is empty, return None
    if int_list == []:
        return None

    # Integer average
    mid = (low + high) // 2

    # If mid == low, final comparison
    if mid == low:
        # Match found
        if int_list[mid] == target:
            return mid
        # Match found in upper edge case
        try:
            if int_list[mid+1] == target:
                return mid+1
        except:
            return None
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