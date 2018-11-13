import random

num_words = 100
text = './purloined.txt'

trigrams = {}
first = ''
second = ''

dictionary = {}

with open(text) as file:
    for line in file:
        line = line.lower()
        line = line.replace('-', ' ')

        new_line = ''
        for letter in line:
            if letter >= 'a' and letter <= 'z' or letter in ' ':
                new_line += letter
        line = new_line

        words = line.split(' ')
        for third in words:
            if first is '' or second is '' or third is '':
                first = second
                second = third
                continue

            if trigrams.get((first, second)) is None:
                trigrams[(first, second)] = {}

            if trigrams[(first, second)].get(third) is None:
                trigrams[(first, second)][third] = 0

            trigrams[(first, second)][third] += 1

            first = second
            second = third

keys = list(trigrams.keys())
length = len(keys)
index = random.randint(0, length-1)
bigram = keys[index]

for key in keys:
    count = 0
    for value in trigrams[key]:
        count += trigrams[key][value]
    for value in trigrams[key]:
        freq = trigrams[key][value]/count
        trigrams[key][value] = freq

error = ''
for i in range(1, num_words+1):
    print(bigram[0], end=' ')
    if i % 10 == 0:
        print()
    target_freq = random.random()
    running_value = 0
    if bigram not in trigrams:
        error = '\n\nBigram does not exist, ending sequence.'
        break
    for value in trigrams[bigram]:
        running_value += trigrams[bigram][value]
        if running_value > target_freq:
            bigram = (bigram[1], value)
            break
print(bigram[1] + error)
