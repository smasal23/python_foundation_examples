# Look at the series below: 1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,.....
# This series is formed as below:
# 1.term(1)=1
# 2.term(2)=2
# 3.term(N)=term(N-1)+term(N-2)for N>2
N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a, b = 1, 2
    for i in range(3, N + 1):
        a, b = b, a + b
    print(b)