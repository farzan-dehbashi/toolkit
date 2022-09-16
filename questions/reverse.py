
def count(string):
    char_dict = dict()
    for char in string:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

print(count("abbcccdddd"))