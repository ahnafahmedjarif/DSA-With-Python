# Function to perform selection sort
def selection_sort(L):
    n = len(L)  # Get the length of the list

    for i in range(0, n-1):
        index_min = i  # Assume the current index is the minimum

        for j in range(i+1, n):
            if L[j] < L[index_min]:  # Find the index of the minimum element
                index_min = j

        if index_min != i:  # Swap if a smaller element is found
            L[i], L[index_min] = L[index_min], L[i]

if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]  # List to be sorted
    print(f"Before sort: {L}")
    selection_sort(L)  # Perform selection sort
    print(f"After sort: {L}")