# this function outputs vowels present in a string
def vowel_generator(str):
    new_str = str.lower()                              # changes every input string to lowercase
    vowels = ["a", "e", "i", "o", "u"]
    vowels_found = []
    for item in new_str:
        if item in vowels:
            vowels_found.append(item)
            no_duplicates = []
            for i in vowels_found:
                if i not in no_duplicates:             # removes duplicated vowels from list "vowels_found"
                    no_duplicates.append(i)
            res = ', '.join(no_duplicates)             # changes a list into a string and separates with a comma
    print("Vowels:", res)


vowel_generator()

     