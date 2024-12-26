# Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based) of the largest element in arr[] that is less than or equal to k. This element is called the "floor" of k. If such an element does not exist, return -1.

def find_floor(arr, k):
    low, high = 0, len(arr)-1
    result = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= k:
            result = mid
            low = mid + 1
        
        if arr[mid] > k:
            high = mid -1

    return result


def test_find_floor():
    arr = [1, 2, 8, 10, 10, 12, 19]
    k = 5
    assert find_floor(arr, k) == 1

    arr = [1, 2, 8, 10, 10, 12, 19]
    k = 20
    assert find_floor(arr, k) == 6

test_find_floor()