n = int(input())

buildings = list(map(int, input().strip().split()))

for i, building in enumerate(buildings):
    left_max = 0
    right_max = 0

    for left in range(0, i):
        if left > left_max:
            left_max = left

    for right in range(i + 1, len(buildings)):
        if right > right_max:
            right_max = right

    left_del = (i - left)