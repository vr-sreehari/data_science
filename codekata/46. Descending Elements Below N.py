userInput = int(input())
arr = list(map(int,input().split()))

sortedArr = sorted(arr)
res=[]

for i in arr:
    if userInput>i:
        res.append(i)

joinedRes=" ".join(map(str,res))

if joinedRes:
    print(joinedRes[::-1])
else:
    print(-1)