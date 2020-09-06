s = input()
n = len(s)
freq = [0 for _ in range(n)]
count = 0
ans = 0

for index, char in enumerate(s):
    if char == "A":
        count += 1
    freq[index] = count

for index, char in enumerate(s):
    if char == "Q":

        for j in range(index+1, n):
            if s[j] == "Q":
                ans += freq[j] - freq[index]

print(ans)
