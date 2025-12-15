def alpha(user_string):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    user_chars = set(user_string.lower())

    used_chars = []
    for char in user_string.lower():
        if char in alphabet and char not in used_chars:
            used_chars.append(char)
    print(' '.join(used_chars))
    

    remaining_alphabet = []
    for char in alphabet:
        if char not in user_chars:
            remaining_alphabet.append(char)

    chunk_size = 5  
    for i in range(0, len(remaining_alphabet), chunk_size):
        chunk = remaining_alphabet[i:i + chunk_size]
        print(' '.join(chunk))

alpha('пайтон')
