# Reverse words

def reverse_words(words):
    words = words.strip()
    words.replace("  ", " ")
    words_arr = words.split(" ")
    return " ".join(words_arr[::-1])

if __name__ == "__main__":
    print(reverse_words(" the sky is blue "))