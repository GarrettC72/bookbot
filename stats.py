def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    lowercase_text = text.lower()
    char_count = {}
    for c in lowercase_text:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] = char_count[c] + 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    sorted_char_count = []
    for k, v in char_count.items():
        sorted_char_count.append({"char": k, "num": v})
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count
    