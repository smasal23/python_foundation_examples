# Find the minimum among 10 numbers.
while True:
    values = list(map(int, input().split()))  # Remember to code the input variable line inside the while loop so as to avoid infinite loop.
    if len(values) == 10:
        break
    print("Required 10 inputs only")

print(min(values))