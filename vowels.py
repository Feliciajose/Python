# function to find vowels in a string
def find_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_list = []
    for char in string:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list

# main program to take user input and call find_vowels() function
string = input("Enter a string: ")
vowel_list = find_vowels(string)
print("The vowels in the given string are:")
for vowel in vowel_list:
    print(vowel)