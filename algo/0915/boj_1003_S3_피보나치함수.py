testcase = int(input())
for _ in range(testcase):

    n = int(input())

    if n != 1 and n != 0:
        arr = [0 for _ in range(n + 1)]
        arr[-1] = 1
        # print(arr)
        for i in reversed(range(len(arr))):
            if i == 1:
                break
            # print(i, ":")
            arr[i - 2] += arr[i]
            arr[i - 1] += arr[i]
            # print(arr)

        print(arr[0], arr[1])

    else:
        if n==0:
            print("1 0")
        else:
            print("0 1")