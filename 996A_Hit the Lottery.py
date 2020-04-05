n = int(input())
bills = [100, 20, 10, 5, 1]
ans = 0
bill = 0

while n:

    cur_bill = bills[bill]
    quotient = n // cur_bill

    if quotient == 0:
        bill += 1

    else:
        ans += quotient
        n %= cur_bill

print(ans)
