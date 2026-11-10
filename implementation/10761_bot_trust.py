T = int(input())

for tc in range(1, T + 1):
    data = input().split()

    N = int(data[0])

    commands = []
    idx = 1

    for _ in range(N):
        robot = data[idx]
        button = int(data[idx + 1])

        commands.append((robot, button))
        idx += 2

    pos_O = 1
    pos_B = 1

    time = 0

    last_O = 0
    last_B = 0

    for robot, button in commands:

        if robot == 'O':
            distance = abs(button - pos_O)
            moved_time = time - last_O
            remain = max(0, distance - moved_time)

            time += remain + 1

            pos_O = button
            last_O = time

        else:
            distance = abs(button - pos_B)
            moved_time = time - last_B
            remain = max(0, distance - moved_time)

            time += remain + 1

            pos_B = button
            last_B = time

    print(f'#{tc} {time}')
