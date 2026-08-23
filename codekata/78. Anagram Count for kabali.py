N = int(input())
arr=[]
for i in range(N):
    word = input()
    arr.append(word)
count=0
for i in arr:
    if(sorted(i)==sorted("kabali")):
        count+=1

print(count)

