userInput = input()
userInput1 = input().split()

res = []
count = 0;
for i in userInput1:
    if(i=='0' and count<2):
        count+=1
        if count<2:
            res.append(userInput1[int(i)+1])


if(count>1):
    print(" ".join(res))
else:
    print(-1)

"""
n = int(input())
arr = input().split()

try:
    first = arr.index('0')
    second = arr.index('0', first + 1)

    if second == first + 1:
        print(-1)
    else:
        print(" ".join(arr[first + 1:second]))
except ValueError:
    print(-1)
"""