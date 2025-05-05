def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowercase_text = text.lower()    
    characters_ocurrence = {}

    for char in lowercase_text:           
        if char in characters_ocurrence:
            characters_ocurrence[char] += 1
        else: 
            characters_ocurrence[char] = 1

    return characters_ocurrence

def chars_dict_to_sorted_list(num_chars_dict):
    list_of_dicts = []
    for ocurrence in num_chars_dict:            
        list_of_dicts.append({"char": ocurrence, "num": num_chars_dict[ocurrence]})

    def get_num(item):
        return item["num"]

    list_of_dicts.sort(key=get_num, reverse=True)
    return list_of_dicts

