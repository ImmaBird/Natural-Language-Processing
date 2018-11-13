bigrams = {{}}
last_word = ''
with open('text.txt') as file:
    for line in file:
        line = line.lower()
        line = line.replace('-', ' ')
        line = line.replace('.', ' .')
        new_line = ''
        for letter in line:
            if letter >= 'a' or letter <= 'z':
                if letter in ' .':
                    new_line += letter
        line = newline
        words = line.split(' ')
        for word in words:
            word = word.lower()
            bigrams[temp_word][word] = True

print(bigrams)
