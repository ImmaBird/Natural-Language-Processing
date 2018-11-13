# Spell Correcter
# Bradley Rawson Jr


# add: hap( )y -> hap(p)y index: 0-5
def insert(word, letter, index):
    return word[:index] + letter + word[index:]


# delete: happy(y) -> happy( ) index: 0-4
def remove(word, index):
    return word[:index] + word[index + 1:]


# substitution: hap(y)y -> hap(p)y index: 0-4
def replace(word, letter, index):
    return word[:index] + letter + word[index + 1:]


# transposition: (ah)ppy -> (ha)ppy index: 0-3
def swap(word, index):
    return word[:index] + word[index + 1] + word[index] + word[index + 2:]


# gets the permutations of strings
def get_variations(variations, new_variations):
    for word in variations:
        if word is '':
            continue
        length = len(word)

        # every variation of adding a letter
        for letter in range(ord('a'), ord('z')):
            letter = chr(letter)
            for index in range(0, length + 1):
                new_variations.add(insert(word, letter, index))

        # every variation of substituting a letter
        for letter in range(ord('a'), ord('z')):
            letter = chr(letter)
            for index in range(0, length):
                new_variations.add(replace(word, letter, index))

        # evey variation of deleting a letter
        for index in range(0, length):
            new_variations.add(remove(word, index))

        # every variation of transposing two letters
        for index in range(0, length - 1):
            new_variations.add(swap(word, index))


# returns a suggestion for a misspelled word
def correct_word(word, edit_distance=1):
    print('----' + word + '----')
    if word in dictionary:
        print("\"" + word + "\" is correct")
        return word

    variations = [{word}]
    suggestion = ""

    for i in range(0, edit_distance):
        variations.append({''})
        get_variations(variations[i], variations[i + 1])

    for hash_maps in variations:
        for variation in hash_maps:
            if variation in dictionary:
                if dictionary[variation] > dictionary[suggestion]:
                    print(variation + ': ' + str(dictionary[variation]))
                    suggestion = variation

    if suggestion is not '':
        return suggestion
    else:
        return word


# strips the word
def strip_word(word):
    stripped_word = ''
    for letter in word:
        if letter >= 'a' and letter <= 'z':
            stripped_word += letter
        elif letter >= 'A' and letter <= 'Z':
            stripped_word += chr(ord(letter) + 32)
        elif letter in accepted_characters:
            stripped_word += letter
    return stripped_word


input_file = './test.txt'
dictionary_file = "./dict_with_freq.txt"
output_file = "./output.txt"
dictionary = {}
accepted_characters = "'"

# makes empty strings unfavorable
dictionary[''] = (-2)

# load dictionary into memory
with open(dictionary_file) as file:
    for line in file:
        tokens = line.split(':')
        dictionary[tokens[0]] = int(tokens[1])

# corrects the words in an input file and writes them to an output file
with open(input_file) as input:
    with open(output_file, 'w') as output:
        for line in input:
            line = line.split()
            correct_line = ""
            for word in line:
                stripped_word = strip_word(word)
                if stripped_word is not '':
                    correct_line += (correct_word(stripped_word, 2) + " ")
            output.write(correct_line[:-1] + '\n')
