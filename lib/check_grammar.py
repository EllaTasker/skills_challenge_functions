# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter 
# and ends with a suitable sentence-ending punctuation mark.


#name check_grammar(). Parameters: string. What it returns: false if punctuation
#not observed and true if both the frst letter is a caital and if it ends with 
#punctuation e.g. ',' '.' '?'. 

# def check_grammar(string):
#     if string[0].isupper() and string[-1] == '.':
#         return True
#     elif string[0].isupper() and string[-1] == '!':
#         return True
#     elif string[0].isupper() and string[-1] == '?':
#         return True
#     elif string.islower():
#         return False
#     elif string[0].isupper():
#         return False
#     else:
#         return False    
    

# the above code works but i am going to try and refactor. 
def check_grammar(string):
    if string[0].isupper() and string[-1] in {'.', '!', '?'}:
        return True
    else:
        return False

    