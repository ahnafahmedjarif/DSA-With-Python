# Write a program to search for a number in a 2D list (list of lists).

def linear_search(L, x):
    n = len(L)                    

    for i in range(n):
        for j in range(len(L[i])):  
            if L[i][j] == x:
                return (i, j)
            
    return -1


def test_linear_search():
    L = [[2, 4, 7], [6, 3, 10], [1, 5, 9]]

    assert linear_search(L, 1) == (2, 0)
    assert linear_search(L, 4) == (0, 1)
    assert linear_search(L, 10) == (1, 2)
    assert linear_search(L, 11) == -1

    print("All tests pass")

test_linear_search()