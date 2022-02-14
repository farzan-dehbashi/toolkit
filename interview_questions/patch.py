def patch(c, n):
    collection = [1]
    reachable = []
    for i in range (1,n+1,1):
        if i in collection:
            reachable.append(i)
        elif i in reachable:
            pass
        else:
            for element in collection:
                reachable.append(element + i)
            collection.append(i)
            reachable.append(i)
            reachable.sort()
        print(f'i = {i}, collection= {collection}, reachable= {reachable}')
        
    return (reachable, collection)
print(patch([1,2,3], 4))