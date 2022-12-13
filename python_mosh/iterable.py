sentence = "here is me ghavatal javiyal almalekiyal ordoniayl"
max_o, max_c = 0, ""
for char in sentence:
    if sentence.count(char) > max_o:
        max_o, max_c = sentence.count(char), char
print(max_o, max_c)
