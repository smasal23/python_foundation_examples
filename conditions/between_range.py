# Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
L = float(input())
N_1, R = map(float, input().split())

if L > N_1 < R:  # it should be L <= N_1 <= R
    print("yes")
else:
    print("no")