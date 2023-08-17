# Creator: Apurv Manjrekar
# CSE 2050 Mod 1 HW
# Prof: Dr. Kloub

import letters # imports module letters

def highest_freq(text):
    "Returns the letter that has the highest frequency in a given text."
    # Checks if the text is empty
    if(text == ""):
        print("The string is empty!", "\n")
        return "The string is empty!"
    
    # Calls letter_count and letter_frequency from letters
    dict_count = letters.letter_count(text)
    dict_freq = letters.letter_frequency(dict_count)
    greatest_freq = 'a'

    # Finds the letter with the greatest frequency in text
    for key in dict_freq:
        if(dict_freq[key] >= dict_freq[greatest_freq]):
            greatest_freq = key

    # Prints out the letter with the greatest frequency and its frequency as a tuple
    tup = (greatest_freq, dict_freq[greatest_freq])
    print(tup, "\n")
    
    return tup

if(__name__ == "__main__"):
    # Testing highest_freq()
    expected_highest_freq = ("c", 0.286)
    actual_highest_freq = highest_freq('aBBcCdf(^*33 Hfccdv R')
    assert(expected_highest_freq == actual_highest_freq)

    # Testing with empty string
    expected_highest_freq = "The string is empty!"
    actual_highest_freq = highest_freq("")
    assert(expected_highest_freq == actual_highest_freq)