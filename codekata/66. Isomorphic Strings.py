def isomorphic(a,b):
    if len(a) != len(b):
        return "no"
    
    set1 = {}
    set2 = {}
    
    for i in range(len(a)):
        x = a[i]
        y = b[i]
        
        if x in set1 and set1[x] != y:
            return "no"
        
        if y in set2 and set2[y] != x:
            return "no"
            
        set1[x] = y
        set2[y] = x
    
    return "yes"

a,b = input().split(" ")




print(isomorphic(a,b))


