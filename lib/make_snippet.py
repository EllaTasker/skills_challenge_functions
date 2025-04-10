# A function called make_snippet that takes a string as an argument and 
# returns the first five words and then a '...' if there are more than that.

def make_snippet(string):
    my_string = string.split()
    if len(my_string) > 5:
        return ' '.join(my_string[:5]) + '...'
    else:
        return ' '.join(my_string)