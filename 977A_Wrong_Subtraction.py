inputs = input()
inputs_mod = inputs.split()

n = int(inputs_mod[0])
k = int(inputs_mod[1])

# n = int(raw_input())
# k = int(raw_input())

while k > 0:

    last_digit = n%10

    if last_digit == 0:
        n /= 10
    else:
        n -= 1

    k -= 1

print(int(n))
