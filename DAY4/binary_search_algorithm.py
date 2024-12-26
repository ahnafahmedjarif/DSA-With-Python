# Function to perform binary search
def binary_search(L, x):
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if L[mid] == x:  # Check if the middle element is the target
            return mid  # Return the index if found
        
        if L[mid] < x:  # If the middle element is less than the target
            low = mid + 1  # Move the low pointer to the high half
        else:  # If the middle element is greater than the target
            high = mid - 1  # Move the high pointer to the low half

    return -1  # Return -1 if the target is not found

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # List to search in

    for x in range(1, 11):
        position = binary_search(L, x)  # Perform binary search

        if position == -1:
            if x in L:
                print(f"{x} is in L, but function returned -1")  # Error message if x is in L but not found
            else:
                print(f"{x} not in list")  # Message if x is not in L
        else:
            print(f"{x} found at index {position}")  # Message if x is found