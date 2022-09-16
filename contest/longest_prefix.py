def find_longest():
    words = ["dog","racecar","car"]
    lcpm = words[0]
    for word in words[1:]:
        for index, char in enumerate(lcpm):
            if len(word) > index:
                if not word[index] == char:
                    lcpm = lcpm[:index]
            else:
                lcpm = lcpm [:index]
    return lcpm

print(find_longest())