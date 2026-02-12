# Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.

N = int(input())

def smallest_power_2(N):
    power = 1
    while power <= N:
        power = power * 2
    return power

print(smallest_power_2(N))