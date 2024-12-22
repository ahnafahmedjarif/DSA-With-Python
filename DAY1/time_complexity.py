# Time Complexity Examples

# Constant time complexity O(1)
num_first = 10
num_second = 20
result = num_first + num_second # O(1)

# Constant time complexity O(1)
n = int(input())
result = n * (n + 1) // 2 # O(1)

# Linear time complexity O(n)
n = int(input())
result = 0
for i in range(1, n + 1):
    result += i # O(n)