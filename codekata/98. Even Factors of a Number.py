N = int(input())

out = ""

for i in range(1,N+1):
    if N%i == 0:
        if i%2==0:
            out += " " +str(i)

if out:
  print(out.strip())
else:
  print(-1)