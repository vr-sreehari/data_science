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

