# Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

def first_repeating_element(L):
    n = len(L)
    min_index = n

    for i in range(n):
        for j in range(i+1, n):
            if L[i] == L[j]:
                min_index = min(min_index, j)
        
    if min_index == n:
        return -1
    
    return L[min_index]
    
def test_first_repeating_element():
    L = [2, 4, 5, 7, 5]
    assert first_repeating_element(L) == 5

    L = [1, 2, 3, 4, 1]
    assert first_repeating_element(L) == 1

    print("All test done!")

test_first_repeating_element()