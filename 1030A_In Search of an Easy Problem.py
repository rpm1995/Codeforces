n = int(input())
ratings = list(map(int, input().split()))

is_easy = True

for rating in ratings:
    if rating == 1:
        is_easy = False
        break

if is_easy:
    print("EASY")
else:
    print("HARD")
