# Check for Pangram
# Determine if a string contains every letter of the English alphabet at least once.
# Use a set for comparison with the set of lowercase alphabets.

def alphabets_in_string(para):
    sett=set()
    for let in para:
        if let.isalpha() and let.lower() not in sett:
            sett.add(let.lower())

    if len(sett)==26:
        return True
    return False

para="abcdefghijklmnopqrstuvwxyz"
print(alphabets_in_string(para))