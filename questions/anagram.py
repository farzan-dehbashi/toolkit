

def is_anagram(string1, string2):
    is_anagram = False
    string1_dict = {}
    for char in string1:
        if char in string1_dict.keys():
            string1_dict[char] += 1
        else:
            string1_dict[char] = 1
    string2_dict = {}
    for char in string2:
        if char in string2_dict.keys():
            string2_dict[char] += 1
        else:
            string2_dict[char] = 1
    if string2_dict == string1_dict:
        is_anagram = True
    return is_anagram


if __name__ == '__main__':
    string1 = 'danger'
    string2 = 'garden'
    print(is_anagram(string1, string2))