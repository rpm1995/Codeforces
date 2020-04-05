n = int(input())
ans = 0

if n == 2:
    print(1)

else:
    for leader in range(1, n):
        employees = n - leader

        if employees % leader == 0:
            ans += 1

    print(ans)
