import enchant
from difflib import SequenceMatcher


def sentence_suggestion(input_text, list_of_words):
    d = enchant.Dict('en_US')
    input_text = input_text.strip().split()
    list_of_words = list_of_words.strip().split()
    for i in range(len(input_text)):
        if not d.check(input_text[i]):
            print(input_text[i], SequenceMatcher(None, input_text[i], list_of_words[i]).ratio(), list_of_words[i], d.suggest(input_text[i])[0])
    return d.suggest(input_text[i])[0]


with open('dataset.txt', 'r') as dataset:
    for line in dataset:
        line

input_word = input("Enter word: ")
print('Did you mean: ', sentence_suggestion(input_word, line))

