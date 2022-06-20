import string


def suggest_word(input_text, word_in_data):
    similar_words = []
    for i in range(len(word_in_data)):
        if word_in_data[i].startswith(input_text):
            similar_words.append(word_in_data[i].replace('.', ""))
    similar_words = list(set(similar_words))
    return similar_words


with open('dataset.txt', 'r') as dataset:
    for line in dataset:
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.strip().split()

input_word = input("Enter word: ")
word_list = input_word.strip().split(' ')[-1]
print(suggest_word(input_word, words))
