# A function called count_words that takes a string as an
# argument and returns the number of words in that string.
def count_words(string):
    my_string = string.split()
    print(len(my_string))   
    return len(my_string) 