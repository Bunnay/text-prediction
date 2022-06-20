import string
lexicon = {}


def update_lexicon(current: str, next_word: str) -> None:
    # Add the input word to the lexicon if it in there yet.
    if current not in lexicon:
        lexicon.update({current: {next_word: 1}})
        return

    # Recieve te probabilties of the input word.
    options = lexicon[current]

    # Check if the output word is in the propability list.
    if next_word not in options:
        options.update({next_word: 1})
    else:
        options.update({next_word: options[next_word] + 1})

    # Update the lexicon
    lexicon[current] = options


# Populate lexicon
with open('dataset.txt', 'r') as dataset:
    for line in dataset:
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.strip().split(' ')
        for i in range(len(words) - 1):
            update_lexicon(words[i].lower(), words[i + 1].lower())

# Adjust propability
for word, transition in lexicon.items():
    transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
    lexicon[word] = transition

# Predict next word
line = input('Enter word: ')
word = line.strip().split(' ')[-1].lower()
if word not in lexicon:
    # print('Word not found')
    next_words = []
else:
    options = lexicon[word]
    sortAsc = dict(sorted(options.items(), key=lambda item: item[1], reverse=True)).keys()
    next_words = [k for k in sortAsc]
    if line in next_words:
        next_words.remove(line)
    print(line + ' ' + str(next_words))
