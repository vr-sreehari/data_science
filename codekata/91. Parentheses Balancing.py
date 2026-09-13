str = input()

open=[]
close=[]

for i in str:
    if i=='(':
        open.append(i)
    else:
        close.append(i)
        
if len(open)==len(close):
    print("yes")
else:
    print("no")

