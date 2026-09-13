N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

count = 0

for i in range(N):
    for j in range(N):

        if matrix[i][j] == 1:

            is_island = True

            directions = [
                (-1, 0),   # up
                (1, 0),    # down
                (0, -1),   # left
                (0, 1)     # right
            ]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N:
                    if matrix[ni][nj] == 1:
                        is_island = False
                        break

            if is_island:
                count += 1

print(count if count > 0 else -1)