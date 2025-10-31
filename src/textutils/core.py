def capitalize_sentences(text: str) -> str:
    import string
    if not text:
        return text


    lower_text = text.lower()
    sentence_enders = ('.', '!', '?')
    result = lower_text[0].upper() + lower_text[1:]
    

    for i, char in enumerate(result):
        if char in sentence_enders:
            try:
                j = i + 1 
                while j < len(result) and result[j] == ' ':
                    j += 1
                if j < len(result):
                    result = result[:j] + result[j].upper() + result[j+1:]
                    
            except IndexError:
                break 

    return result