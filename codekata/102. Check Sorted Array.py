N = input()
arr = list(map(int,input().split()))

sortAsc = sorted(arr)
sortDes = sorted(arr,reverse=True)

if arr==sortAsc or arr==sortDes:
  print("yes")
else:
  print("no")

