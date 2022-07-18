def shuffle(s, indices):
    res = ''
    for i, char in enumerate(s):
        res += s[indices[i]]
    return res
    
print(shuffle(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))