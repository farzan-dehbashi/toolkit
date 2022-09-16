from collections import Counter

def sub_arr(arr):
    ratio = 0
    ratios = []
    for cur in range(0, len(arr), 1):
        if arr[cur] == 0:
            ratio -=1
        elif arr[cur] == 1:
            ratio += 1
        ratios.append(ratio)
    print(ratios)
    c = Counter(ratios)
    el, oc = c.most_common()[0]
    start = ratios.index(el)
    print(start)
    end = len(ratios) - ratios[::-1].index(el) -1
    print(end)
    return (start, end)

print(sub_arr([0,0,1,0,1,0,1,1]))