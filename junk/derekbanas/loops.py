import random

for i in range(0, 10):
    print(i, " ", end="")

print()

for i in [1, 2, "xd"]:
    print(i, " ", end="")

print()

matrix = [
    [1, 2, 3],
    [1, 2, 2],
    [3, 3, 1]
]

print("====")

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], " ", end="")
    print()


print("Quessing 0")
num = random.randrange(0, 100)
while num != 0 :
    num = random.randrange(0, 100)
    print(num)

print("\nPrinting even numbers :")

i = 0
while (i <= 20):
    if (i%2 == 0):
        print(i)
    i += 1
