# Creator: Apurv Manjrekar
# CSE 2050 Mod 1 HW
# Prof: Dr. Kloub

import string

def letter_count(text):
    """Returns a dictionary of the count/occurence of each letter of 
    the English Alphabet in the parameter.
    """
    # Creating an empty dictionary and a count variable initialized to 0
    dictionary = {}

    # Iterating through each letter in the alphabet 
    for letter in string.ascii_lowercase:
        # Adding the occurence of each letter in alphabet to the empty dictionary
        dictionary[letter] = text.lower().count(letter)

    return dictionary # Returns dictionary of occurences

def letter_frequency(dict_letters):
    """Returns a dictionary of the frequency of each letter of the English
    Alphabet in a given text based on a dictionary of the count/occurence 
    of each letter of the English Alphabet in a given text
    """
    # Creating an empty dictionary and a total variable initialized to 0
    total = 0
    dict_freq = {}

    # Iterating through each key in dict_letters
    for key in dict_letters:
        # Adding the value at each key to total
        total += dict_letters.get(key)
    
    # Iterating through each key in dict_letters
    for key in dict_letters:
        # Setting the value of key in dict_freq to the ratio between the value at key in dict_letters and total
        if(total == 0):
            dict_freq[key] = 0
        else:
            dict_freq[key] = round(dict_letters.get(key)/total, 3)
    
    return dict_freq # Returns dictionary of frequencies

if(__name__ == "__main__"):
    # Testing if letter_count() works
    expected_count = {'a': 1, 'b': 2, 'c': 4, 'd': 2, 'e': 0, 'f': 2, 'g': 0, 'h': 1,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 1,
    's': 0, 't': 0, 'u': 0, 'v': 1, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    actual_count = letter_count('aBBcCdf(^*33 Hfccdv R')
    assert(expected_count == actual_count)

    # Testing if letter_count() works
    expected_count2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    actual_count2 = letter_count('')
    assert(expected_count2 == actual_count2)

    # Testing if letter_frequency() works
    expected_frequency = {'a': 0.071, 'b': 0.143, 'c': 0.286, 'd': 0.143, 'e': 0, 'f': 0.143, 'g': 0, 'h': 0.071,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0.071,
    's': 0, 't': 0, 'u': 0, 'v': 0.071, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    actual_frequency = letter_frequency(letter_count('aBBcCdf(^*33 Hfccdv R'))
    assert(actual_frequency == expected_frequency)

    expected_frequency2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    actual_frequency2 = letter_frequency(letter_count(''))
    assert(actual_frequency2 == expected_frequency2)