L,R = map(int,input().split())
    
for i in range(1,R*L):
    if (i%L==0 and i%R==0):
        print(i)
        break
    

"""
L, R = map(int, input().split())

for i in range(1, L * R + 1):
    if i % L == 0 and i % R == 0:
        print(i)
        break
"""