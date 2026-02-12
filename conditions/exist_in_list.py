# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
N, K = map(int, input().split())
List_N = list(map(int, input().split()))

if K in List_N:
    print('yes')
else:
    print('no')