import enchant


def suggested_word(list_of_words):
    wrong = []
    correct = []
    d = enchant.Dict('en_US')
    # check the individual element in list
    for i in range(len(list_of_words)):
        # if word doesn't exist
        if not d.check(str(list_of_words[i])):
            wrong.append(list_of_words[i])
        else:
            correct.append(list_of_words[i])
    return correct

list_suggested = enchant.Dict('en_US').suggest(input_word)
print(suggested_word(list_suggested))