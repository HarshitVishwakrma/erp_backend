from num2words import num2words

def convert_to_words(amount):
    # Convert float or int to words, using Indian English currency style
    return num2words(amount, to='currency', lang='en_IN')
