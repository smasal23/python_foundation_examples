# You are given with Principle amount($), Interest Rate(%) and Time (years) in that order.
# Find Simple Interest. Print the output up to two decimal places (Round-off if necessary). (S.I. = PTR/100)

P, R, T = map(float, input().split())

def Simple_Interest(P, R, T):
    SI = (P * T * R) / 100
    return f"{SI:.2f}"

print(Simple_Interest(P, R, T))