# determines the frequency of words as they appear in a sample text
# the frequencies are stored along side their respective words in a
# text file one word per line word and frequency denoted by a colon
# Bradley Rawson Jr.

dictionary_file = './dictionary.txt'
sample_text_file = './sample_text.txt'
accepted_characters = "'"
dictionary = {}
word_count = 0

# create dictionary as dict
with open(dictionary_file) as file:
    for line in file:
        dictionary[line.strip('\n')] = 0

# counts the frequency of words in the sample text
with open(sample_text_file, encoding='utf-8') as sample_text:

    # reads the words
    for line in sample_text:
        line = line.replace('-', ' ')
        words = line.split()
        for word in words:

            # strips the word
            stripped_word = ""
            for letter in word:
                if letter >= 'a' and letter <= 'z':
                    stripped_word += letter
                elif letter >= 'A' and letter <= 'Z':
                    stripped_word += chr(ord(letter) + 32)
                elif letter in accepted_characters:
                    stripped_word += letter

            # tallies the word in the dictionary
            if stripped_word is not '':
                if stripped_word in dictionary:
                    dictionary[stripped_word] += 1
                    word_count += 1

# creates a new dictionary with the frequencies in our sample text included
with open('./dict_with_freq.txt', 'w') as file:
    for key, value in dictionary.items():
        file.write(key + ':' + str(value) + '\n')
