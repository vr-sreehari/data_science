N,K = map(int,input().split())

res = False

for i in range(1,K):
  if (K**i)==N:
    res = True
    break

if res:
  print("yes")
else:
  print("no")

"""
N, K = map(int, input().split())

if N == 1:
    print("yes")
elif K <= 1:
    print("yes" if N == K else "no")
else:
    power = K

    while power < N:
        power *= K

    if power == N:
        print("yes")
    else:
        print("no")
"""