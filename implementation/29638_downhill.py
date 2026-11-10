T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 1
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            answer = 0
            break

    print(f"#{tc} {answer} ")
