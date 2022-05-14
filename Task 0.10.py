# this function outputs out common letters shared amongst two strings 

def common_letters(str1, str2):

    str1_lower = str1.lower()                     # changes input strings into lowercase
    str2_lower = str2.lower()
    
    common_letters_list = []
    for item in str1_lower:
        if item in str2_lower:
            common_letters_list.append(item)
            res = ', '.join(common_letters_list)  # changes a list into a string


    print("Common letters: ", res)


common_letters()
