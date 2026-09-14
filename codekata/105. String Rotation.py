S,K = input().split()

res = ""

for i in range(int(K)):
  res += S[i]

splitArr=S.split(res)

print("".join(splitArr[1]) + res)

"""
S, K = input().split()

K = int(K)

print(S[K:] + S[:K])
"""