# This method is used by pytest. To install pytest, run: pip install pytest
# To test it, type in the terminal: pytest third_method.py

def average(L):
    if not L:
        return None

    return sum(L) / len(L)

def test_average():
    assert 3.0 == average([1, 2, 3, 4, 5])