def get_first_non_repeating_char(string):
    first_char = None
    hashmap = {}
    for char in string:
        if char in hashmap.keys():
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    for char in string:
        if hashmap[char] == 1:
            first_char = char
            break
    return first_char


if __name__ == '__main__':
    string = 'aaabbbcdeeeff'
    print(get_first_non_repeating_char(string))