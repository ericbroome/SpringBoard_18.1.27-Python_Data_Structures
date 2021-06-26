setofwords = {"hello", "HeY", "yO", "yEs", "Eric", "Erythritol", "everyone", "noboDy", "someone", "fuggedaboudit"}
setofchars = {'e', 'F', 'H'}
def print_upper_words(words):
    """Function to print words in all uppercase"""
    for word in words:
        print(word.upper())

def get_words_beginning_with(words, char):
    """Return a set of words beginning with a specified character"""
    retval = set()
    if(len(char) != 1):
        print(f"char argument must be a single character and you passed {len(char)} characters")
        return []
    for word in words:
        if(word.upper().startswith(char.upper())):
            retval.add(word)
    return retval

def get_words_beginning_with_one_of(words, chars):
    """Return a set of words beginning with a specified character"""
    retval = set()
    if(type(chars) != "set" and type(chars) != "dict" and type(chars) != "array" and len(chars) <= 0):
        print(f"char argument must be a collection of single characters")
        return []
    for word in words:
        for char in chars:
            if(word.upper().startswith(char.upper())):
                retval.add(word)
    return retval

# First we'll print them all out in uppercase
print("# First we'll print them all out in uppercase")
for word in setofwords:
    print(word.upper())

# Now we'll use the function to print the mall out in uppercase
print("\n# Now we'll use the function to print them all out in uppercase")
print_upper_words(setofwords)

# Now we'll print - in uppercase - only words beginning with e (in upper or lowercase)
print("\n# Now we'll print - in uppercase - only words beginning with e (in upper or lowercase)")
print_upper_words(get_words_beginning_with(setofwords, 'e'))

# Now we'll print - in uppercase - only words beginning with a letter.upper() from a set

print("\n# Now we'll print - in uppercase - only words beginning with a letter.upper() from a set {0}".format(setofchars))
print_upper_words(get_words_beginning_with_one_of(setofwords, setofchars))


 