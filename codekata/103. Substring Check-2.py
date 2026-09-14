s1,s2 = input().split()

res = True

for i in s2:
   if(s1.find(i)==-1):
     res = False

if res:
  print("yes")
else:
  print("no")

