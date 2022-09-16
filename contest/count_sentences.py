sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max = 0
for sentence in sentences:
    words = 0
    spaces = 0
    for char in sentence:
        if char == " ":
            spaces += 1
        if spaces == 0 and len(sentence) > 0:
            words = 1
        if spaces == 1 and len(sentence) > 1:
            words = 1
        else:
            words = spaces + 1
    if words > max:
        max = words
print(max)