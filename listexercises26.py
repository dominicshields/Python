def listutil(mode,lst,val,pos):
    if mode == "count":
            count = 0
            for x in range(len(lst)):
                if lst[x] == val:
                    count += 1
            return count
    if mode == "in":
            for x in range(len(lst)):
                if lst[x] == val:
                    return True
            return False  
    if mode == "reverse":
            cnt = 0
            z = []
            for x in range(len(lst)-1, -1, -1):
                z.append(lst[x])
            return z         
    if mode == "index":
            idx = -1
            for x in range(len(lst)):
                idx += 1
                if lst[x] == val:
                    return idx
            return idx    
    if mode == "insert":
            lst[pos:pos] = val
            return lst
        
#count, in, reverse, index, insert

lst = ["AB","CD","EFG",7,99,"Elephant",6]
mode = "insert"
val = "XX"
pos = 2
print("Mode '",mode,"' found =",listutil(mode,lst,val,pos),"with input val",val)