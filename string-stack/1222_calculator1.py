for tc in range(1, 11):
    N = int(input())
    arr = input()
 
    result = 0
 
    for char in arr:
        if char != '+':
            result += int(char)
 
    print(f"#{tc} {result}")
