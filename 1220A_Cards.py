n = int(input())
string = input()

o_number = 0
zeros = 0
ones = 0
ans = ""

for char in string:
    if char == 'o':
        o_number += 1
    elif char == 'z':
        zeros += 1

ones = o_number - zeros

while ones > 0 or zeros > 0:
    if ones:
        ans += "1 "
        ones -= 1
    elif zeros:
        ans += "0 "
        zeros -= 1

print(ans)
