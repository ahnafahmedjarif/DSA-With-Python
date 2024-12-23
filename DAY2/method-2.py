# Testing a function using asseryion
def average(L):
    if not L:
        return None

    return sum(L) / len(L)

if __name__ == "__main__":
    # Test case
    L = [1, 2, 3, 4, 5]
    expected_avg = 3.0
    
    # Assert to check if the test passed or failed
    assert expected_avg == average(L), "Test failed"
    print("Test passed")