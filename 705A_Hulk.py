n = int(input())
ans = ""

for current in range(1, n+1):

    if current % 2 == 1:
        ans += "I hate "
    else:
        ans += "I love "

    if current == n:
        ans += "it"
    else:
        ans += "that "

print(ans)
