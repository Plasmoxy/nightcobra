import sys

def add(x, y):
    return x + y

print(add(1, 2))

avg = lambda arr: sum(arr)/len(arr)
print(avg([1, 2]))

name = input("Enter your name: ")
print("Your name is", name)