

def d(number,arr):

    if not arr[number]:
        return

    letters = list(str(number))
    for letter in letters:
        number += int(letter)
    if number <= 10000 :
        d(number, arr)
        arr[number] = False

arr = [True for _ in range(10001)]
for i in range(1, 10001):
    if arr[i]:
        d(i, arr)

for index in range(1, len(arr)) :
    if(arr[index]) :
        print(index)