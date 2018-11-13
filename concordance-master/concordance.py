input_file = open('./input.txt', 'r')
output_file = open('./output.txt', 'w')
list_of_function_words = open('./function_words.txt', 'r')
accepted_characters = "-'"
function_words = {}
included_words = {}


def strip_word(word):
    stripped_word = ""
    for letter in word:
        if letter >= 'a' and letter <= 'z':
            stripped_word += letter
        elif letter >= 'A' and letter <= 'Z':
            stripped_word += chr(ord(letter) + 32)
        elif letter in accepted_characters:
            stripped_word += letter
    return stripped_word


for line in list_of_function_words:
    line = line.replace('\n', '').split(' ')
    for word in line:
        word = strip_word(word)
        function_words[word] = None

i = 0
for line in input_file:
    line = line.replace('\n', '')
    words = line.split(' ')
    i += 1
    for word in words:
        word = strip_word(word)
        if word is '':
            continue
        if word in function_words:
            continue
        if word not in included_words:
            included_words[word] = []
        included_words[word].append(str(i) + ') ' + str(line))

sorted_words = sorted(included_words.keys())

for word in sorted_words:
    output_file.write(word + ':\n')
    for line in included_words[word]:
        output_file.write(line + '\n')
    output_file.write('\n')
