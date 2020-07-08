import random
import re

# Read in all the words in one go
with open("./applications/markov/input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
blah_dict = {}

for i in range(len(words) - 1):
    if words[i] not in blah_dict:
        blah_dict[words[i]] = []
        blah_dict[words[i]] = [*blah_dict[words[i]], words[i + 1]]
    else:
        blah_dict[words[i]] = [*blah_dict[words[i]], words[i + 1]]

# TODO: construct 5 random sentences


def blah_constructor():
    blah_sentence = []

    # choose starter word
    while True:
        first_word = random.choice(list(blah_dict.keys()))
        # if capital or quote, then capital
        if re.match("[A-Z]", first_word) or re.match('.["A-Z]', first_word):
            blah_sentence = [*blah_sentence, first_word]
            blah_sentence = [*blah_sentence,
                             random.choice(blah_dict[first_word])]
            break
        else:
            continue

    # keep sentence going
    while True:
        next_word = random.choice(list(blah_dict.keys()))

        # if end word, stop
        if re.search('[!?.].$', next_word):
            blah_sentence = [*blah_sentence, next_word]
            break

        # if starter word, continue
        if re.match("[A-Z]", next_word) or re.match('.["A-Z]', next_word):
            continue

        blah_sentence = [*blah_sentence, next_word]
        blah_sentence = [*blah_sentence, random.choice(blah_dict[next_word])]

    return ' '.join(blah_sentence)


print(blah_constructor())
print('')
print(blah_constructor())
print('')
print(blah_constructor())
print('')
print(blah_constructor())
print('')
print(blah_constructor())
