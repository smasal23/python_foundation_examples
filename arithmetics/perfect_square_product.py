# Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
import math

N, M = map(int, input().split())
product = N * M
root = int(math.sqrt(product))

if root * root == product:
    print("yes")
else:
    print("no")
