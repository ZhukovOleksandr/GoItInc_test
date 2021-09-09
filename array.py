
def cleaning_text(input_text):
    """ Clears the input text from ".,:;!?'" """
    cleaned_text = []
    read_text = input_text.read().split()
    for word in read_text:
        cleaned_text.append(word.strip(".,:;!?'").lower())
    return cleaned_text


def count_word(cleaned_text):
    """ Counts words quantity and do validation by unique words quantity """
    word_quant = {word: cleaned_text.count(word) for word in cleaned_text}
    sorted_word = sorted(word_quant.items(), key=lambda elem: elem[1], reverse=True)
    unique_list = list(filter(lambda elem: elem[1] == 1, sorted_word))
    if len(unique_list) < 3:
        return word_quant.clear()
    else:
        return dict(sorted_word[:3])


if __name__ == '__main__':
    inputed_file = input('Please, enter the file name (use absolute path):\n')
    text = open(inputed_file, 'r')
    print(count_word(cleaning_text(text)))


