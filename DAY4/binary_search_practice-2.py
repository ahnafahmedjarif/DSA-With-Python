# Given an element x and a sorted array, arr[], find the indices of first and last occurrences of the x's in the array.
# If the element is not present in the array, return -1.

def first_last_occurrences_binary_search(arr, k):
    
    def find_first(arr, k):
        low, high = 0, len(arr)-1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                first = mid
                high = mid - 1

            elif arr[mid] < k:
                low = mid + 1

            else:
                high = mid - 1

        return first
    
    def find_last(arr, k):
        low, high = 0, len(arr)-1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                last = mid
                low = mid + 1

            elif arr[mid] < k:
                low = mid + 1

            else:
                high = mid - 1

        return last
    
    first = find_first(arr, k)
    last = find_last(arr, k)
    return first, last


def test_first_last_occurrences_binary_search():
    arr = [1, 2, 2, 3, 4, 5]
    x = 2
    assert first_last_occurrences_binary_search(arr, x) == (1, 2)

    arr = [1, 2, 3, 4, 5]
    x = 2
    assert first_last_occurrences_binary_search(arr, x) == (1, 1)

    arr = [1, 2, 3, 4, 5]
    x = 6
    assert first_last_occurrences_binary_search(arr, x) == (-1, -1)

    print("All test cases passed successfully.")

test_first_last_occurrences_binary_search()