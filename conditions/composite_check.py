# Given a number N, print 'yes' if it is composite else print 'no'.
# for i in range(2, int(N_2**0.5) + 1):
#   if N_2 % i == 0:
#       is_composite = True
#       break
N_2 = int(input())
composite = []

for i in range(1, N_2 + 1):
    if N_2 % i == 0:
        composite.append(i)

if len(composite) > 2:
    print("yes")
else:
    print("no")