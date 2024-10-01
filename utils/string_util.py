import unicodedata
import re

def normalize_string(input_string):
    string = unicodedata.normalize('NFD', input_string)
    
    # Remove accents and other diacritical characters
    string = string = string.encode('ascii', 'ignore').decode('ascii')
    
    # Remove special characters
    string = re.sub('[^A-Za-z0-9 ]+', '', string)
    
    string = string.replace('/', '-').replace(' ', '-')

    return string