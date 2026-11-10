N = int(input())

result = []

for i in range(1, N + 1):
    cnt = 0

    for num in str(i):
        if num == '3' or num == '6' or num == '9':
            cnt += 1

    if cnt > 0:
        result.append('-' * cnt)
    else:
        result.append(i)

print(*result)
