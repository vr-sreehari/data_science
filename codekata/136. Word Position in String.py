S = input().split()
X = input()

result = "-1"

for i,val in enumerate(S):
  if val==X:
    result = i+1
    
print(result)