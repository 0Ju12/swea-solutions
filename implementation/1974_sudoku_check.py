T = int(input())

for tc in range(1, T + 1):
    sdq = []

    for _ in range(9):
        sdq.append(list(map(int, input().split())))

    answer = 1

    # 1. 행 검사
    for r in range(9):
        row = sdq[r]

        if len(set(row))!=9:
            answer = 0
            break


    # 2. 열 검사
    for c in range(9):
        col = []

        for r in range(9):
            col.append(sdq[r][c])

        if len(set(col))!=9:
            answer = 0
            break


    # 3. 3 x 3 검사
    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):

            box = []
            for r in range(sr,sr+3):
                for c in range(sc, sc+3):
                    box.append(sdq[r][c])

            if len(set(box))!=9:
                answer = 0
                break
        if answer ==0:
            break


    print(f"#{tc} {answer}")
