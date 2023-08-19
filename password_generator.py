import string
import secrets
import random


# todo @Author #h4L

# * Only script 


def get_random(list):
    rand = random.choice(list)
    return rand

def generate_password(length,chinise,japanese):
    
    # Define Unicode ranges for Chinese and Japanese alphabets
    chinese_range = (0x4E00, 0x9FFF)
    japanese_range = (0x3040, 0x30FF)
    
    # Create a list of all characters from Chinese and Japanese alphabets
    chinese_characters = [chr(code) for code in range(chinese_range[0], chinese_range[1] + 1)]
    japanese_characters = [chr(code) for code in range(japanese_range[0], japanese_range[1] + 1)]
    
    eng_characters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
    special_chars = string.octdigits
    
    
    # alphabet =  japanese_characters + eng_characters.split() + numbers.split() + punctuation.split() 

    pwd =''
    if chinise and japanese:
        for i in range(length):
            pwd +=get_random(get_random([chinese_characters,japanese_characters,eng_characters,numbers,punctuation]))
    elif chinise:
        for i in range(length):
            pwd +=get_random(get_random([chinese_characters,eng_characters,numbers,punctuation]))
    elif japanese:
        for i in range(length):
            pwd +=get_random(get_random([japanese_characters,eng_characters,numbers,punctuation]))
    else:
        for i in range(length):
            pwd +=get_random(get_random([eng_characters,numbers,punctuation]))
        

    return pwd
    


