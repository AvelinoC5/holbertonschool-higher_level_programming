#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) == 0:
        return (0)
    roman_c = roman_string
    dict_rom = {
        'I': 1,
        'V': 5,
        'X': 10,        
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    count = 0

    for i in range(len(roman_c)):
        if i > 0 and dict_rom[roman_c[i]] > dict_rom[roman_c[i - 1]]:
            count += dict_rom[roman_c[i]] - 2 * dict_rom[roman_c[i - 1]]
        else:
            count += dict_rom[roman_c[i]]
    return count
