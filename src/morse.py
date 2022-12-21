
alphabet = {'а': '.-',
            'б': '-...',
            'в': '.--',
            'г': '--.',
            'д': '-..',
            'е': '.',
            'ж': '...-',
            'з': '--..',
            'и': '..',
            'й': '.---',
            'к': '-.-',
            'л': '.-..',
            'м': '--',
            'н': '-.',
            'о': '---',
            'п': '.--.',
            'р': '.-.',
            'с': '...',
            'т': '-',
            'у': '..-',
            'ф': '..-.',
            'х': '....',
            'ц': '-.-.',
            'ч': '---.',
            'ш': '----',
            'щ': '--.-',
            'ъ': '.--.-.',
            'ы': '-.--',
            'ь': '-..-',
            'э': '..-..',
            'ю': '..--',
            'я': '.-.-'}


def clean_stroke(content):
    lowered_char = str(content).lower()
    if ord(lowered_char) >= 1072 and ord(lowered_char) <= 1103:
        return lowered_char
    else:
        return ''

def Char_to_Morse(character):
    try:
        result = alphabet[clean_stroke(character)]
    except KeyError:
        return ''
    
    return result
