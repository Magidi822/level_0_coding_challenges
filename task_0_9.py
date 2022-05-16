def vowel_generator(str):
    new_str = str.lower()                              
    vowels = ["a", "e", "i", "o", "u"]
    vowels_found = []
    for item in new_str:
        if item in vowels:
            vowels_found.append(item)
            no_duplicates = []
            for i in vowels_found:
                if i not in no_duplicates:             
                    no_duplicates.append(i)
            res = ', '.join(no_duplicates)          
    print("Vowels:", res)


vowel_generator()

     