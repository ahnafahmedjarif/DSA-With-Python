# Find the Kth Smallest Element Using Bubble Sort

def bubble_sort_kth_smallest(arr, k):
    n = len(arr)
    for i in range(k): 
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[k - 1]


array = [7, 10, 4, 3, 20, 15]
k = 3
result = bubble_sort_kth_smallest(array, k)
print(f"The {k}th smallest element is: {result}")