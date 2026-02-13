# Consider the below series: 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8… This series is a mixture of 2 series – all the odd terms
# in this series form even numbers in ascending order and every even term is derived from the previous term using
# the formula (x / 2). Write a program to find the Nth term in this series.

N = int(input().strip())

if N % 2:
    print((N // 2) * 2)
else:
    print((N // 2) - 1)