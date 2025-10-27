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