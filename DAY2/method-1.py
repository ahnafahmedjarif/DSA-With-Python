# Function to test a list of numbers
def average(L):
    if not L:
        return None

    return sum(L) / len(L)

if __name__ == "__main__":
    # Test case
    L = [1, 2, 3, 4, 5]
    expected_avg = 3.0
    result = average(L)

    # Check if the test passed or failed
    if expected_avg == result:
        print("Test passed")
    else:
        print("Test failed")
        print(f"Expected: {expected_avg}")
        print(f"Got: {result}")