N = input()
vowels = ['a','e','i','o','u']
res=""
for i in N:
    if i not in vowels:
        res+=i

if(res):
    print(res[::-1])
else:
    print(-1)


