# Sort Only the First K Elements Using Bubble Sort

def bubble_sort_first_k(arr, k):
    for i in range(k):  
        for j in range(k - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = [9, 7, 6, 8, 2, 3]
k = 4
result = bubble_sort_first_k(array, k)
print(f"Array after sorting first {k} elements: {result}")