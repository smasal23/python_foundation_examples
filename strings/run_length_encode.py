# Given a string aaaabbBccdee, it can be written as a4b2B1c2d1e2.

N = input().strip()
Counts = 1

for i in range(1, len(N)):
    if N[i] == N[i - 1]:
        Counts += 1
    else:
        print(N[i - 1] + str(Counts), end = '')
        Counts = 1

print(N[-1] + str(Counts))