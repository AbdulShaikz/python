def remove_and_strip(string_list,word_to_remove):
    word_to_remove = word_to_remove.strip().lower()
    return [item.strip() for item in string_list if item.strip()!=word_to_remove]

my_list = input("Enter list items(comma separated) : ").split(",")
target_word = input("Enter word to remove : ")

cleaned_list = remove_and_strip(my_list,target_word)
print(cleaned_list)