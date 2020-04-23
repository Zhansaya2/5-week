A = list(map(int, input().split()))
ans = 0
for elem in A:
    if elem > 0:
        ans += 1
print(ans)
