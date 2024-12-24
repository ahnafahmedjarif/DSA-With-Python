# Function to perform linear search
def linear_search(L, x):
    n = len(L)          # Step 1
    i = 0               # Step 2

    while i < n:        # Step 3
        if L[i] == x:   # Step 4
            return i    # Step 5
        
        i += 1          # Step 6

    i = -1              # Step 7

    return i           

# Test function for linear search
def test_linear_search():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

    # Test cases
    assert linear_search(L, 1) == 0
    assert linear_search(L, 5) == 4
    assert linear_search(L, 10) == 9
    assert linear_search(L, 11) == -1

    print("All tests pass")

# Run the test function
test_linear_search()