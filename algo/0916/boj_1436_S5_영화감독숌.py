n = int(input())
if n == 1:
    print(666)
else:
    order = 1
    number = 1666
    while True:
        nums = list(str(number))
        for i, num in enumerate(nums):
            length = len(nums)
            if num == '6':
                if i + 1 < length and nums[i + 1] == '6':
                    if i + 2 < length and nums[i + 2] == '6':
                        order += 1
                        if (order == n):
                            print(number, i)
                        break
        if (order == n):
            break
        number += 1