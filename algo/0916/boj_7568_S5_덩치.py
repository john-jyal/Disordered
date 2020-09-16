number = int(input())

people =[]
for i in range(number):
    people.append(list(map(int, input().split())))


ans = ""
for i in range(number):
    cnt = 0
    wei = people[i][0]
    hei = people[i][1]

    for j in range(number):
        if wei < people[j][0] and hei < people[j][1] :
            cnt += 1

    ans += str(cnt+1) + " "

print(ans)

