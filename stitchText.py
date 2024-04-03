import re

def stitch_strings(first_string, second_string):


    # Convert the strings to lowercase for case-insensitive matching
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Iterate through the first string to find the common suffix
    common_suffix = ''
    for i in range(len(first_string)):
        if second_string.startswith(first_string[i:]):
            common_suffix = first_string[i:]
            break
    
    # If a common suffix is found, combine the strings using it
    if common_suffix:
        return first_string + second_string[len(common_suffix):]
    else:
        # If no common pattern is found, just concatenate the strings
        return first_string + second_string