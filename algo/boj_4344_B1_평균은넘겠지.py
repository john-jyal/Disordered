
testcase = int(input())

for _ in range(testcase):
    data = input().strip().split()
    scores = list(map(int, data[1:]))
    people = int(data[0])
    avg = sum(scores) / people

    cnt = 0

    for score in scores:
        if(score > avg):
            cnt += 1




# testcase = int(input())
#
# for tc in range(testcase) :
#     inp = list(map(int,input().split()))
#     amount = inp[0]
#
#     cnt = 0
#     people = len(inp)
#     tot = sum(map(int,inp)) - amount
#     avg = tot/amount
#
#     for score in range(1, people) :
#         if(inp[score] > avg) :
#             cnt += 1
#
#     res = round(cnt / (people - 1) * 100, 3)
#     print("%.3f" % res+ "%" )




    #ind

#t

# import sys
# input = sys.stdin.readline
#
# test_case = int(input())
#
# for _ in range(test_case):
#     data = input().strip().split(' ')
#     scores = list(map(float, data[1:]))
#     average = sum(scores) / len(scores)
#
#     above = 0
#     for score in scores:
#         if score > average:
#             above += 1
#
#     print(f'{(above/len(scores))*100:.3f}%')


# inp = input().split()
# print(sum(map(int,inp)))
# print(map(int,inp))
# print(inp)
