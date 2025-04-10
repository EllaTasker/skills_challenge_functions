# As a user
# So that I can manage my time
# I want to see an estimate of reading time 
# for a text, assuming that I can read 200 words a minute.

def time_manager(text_length):
    #takes the given text as an argument 
    #need to return the amount of words in a test / 200 to figure out 
    #how many minutes are needed ro read the text 
    # need to turn the string into a list to count the words in it . 
    # if text_length == 0:
    #     return 0
    # elif text_length == 200:
    #     return 1
    # else:
    #     return text_length / 200 
        
#^ this above code works, time to re-factor 
    return text_length / 200