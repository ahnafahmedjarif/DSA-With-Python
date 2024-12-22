# Space Complexity Examples


# O(1) space complexity
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd") # O(1)

# O(n^2) space complexity
n = int(input())

count = 0
for i in range(n):
    for j in range(n):
        count += 1

print(f"n = {n}, count = {count}") # O(n^2)