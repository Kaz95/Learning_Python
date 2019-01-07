# Program that iterates over the given string value and prints the number of occurrences of each character in the string
# Capital characters count separate from lower case.

import pprint   # Formats dictionary output

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}  # Empty dictionary. Used to keep track of character occurrences in the form of key:value pairs.

for character in message:   # Iterate over all characters in a string(including spaces!).
    count.setdefault(character, 0)  # Checks if character has already occurred. If not, add to dictionary as (key: 0)
    count[character] += 1  # Adds 1 to the current characters count. Would return error without above.


"""Capital characters count separate from lower case. Pass to .upper or .lower method first to prevent this. 
    pprint.pformat to return as string for further use in different string methods"""
pprint.pprint(count)
