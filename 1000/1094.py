import sys

input = sys.stdin.readline

X = int(input())
binary_X = bin(X)
# print(type(binary_X), binary_X)
print(binary_X.count('1'))