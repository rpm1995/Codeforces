inputs = input()
weights = list(map(int, inputs.split()))

limak = weights[0]
bob = weights[1]
year = 0

while limak <= bob:

    limak *= 3
    bob *= 2
    year += 1

print(year)
