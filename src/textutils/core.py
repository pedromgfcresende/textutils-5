def is_palindrome(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    inversed = ''
    cleaned_text = ''

    if isinstance(text, int):
        text = str(text)

    if not isinstance(text, str):
        raise ValueError('It should be an word / phrase / number')
    
    for i in range(len(text)):
        if text[i].lower() in letters:
            inversed = text[i].lower() + inversed
            cleaned_text = cleaned_text + text[i].lower()
        
        elif text[i].lower() in numbers:
            inversed = text[i].lower() + inversed
            cleaned_text = cleaned_text + text[i].lower()


    return inversed == cleaned_text

# -------------------------------------------------------------------

def average_word_length(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    lista = text.split()
    number_of_words = len(lista)
    if number_of_words == 0:
        return 0
    a = 0
    for word in lista:
        for letter in word:
            if letter.lower() in alphabet or letter in numbers:
                a +=1
            else:
                continue
    
    return round(a/number_of_words)