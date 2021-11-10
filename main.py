from list_all_words_generator import ListAllWords


def old_list_all_words(p_alphabet, p_min_word_len, p_max_word_len):
    def pos_to_symbols(inp_list: list):
        return [p_alphabet[x] for x in inp_list]

    max_index = len(p_alphabet) - 1
    res = []

    for num_count in range(p_min_word_len, p_max_word_len + 1):
        zero_index = num_count - 1
        num = [0] * num_count
        res.append(pos_to_symbols(num))
        enough = False
        while not enough:
            if num[zero_index] < max_index:
                num[zero_index] += 1
            else:
                # if we will increment number successfully then we reset enough to False
                enough = True
                # instead of enough we will raise StopIteration
                for i in range(zero_index - 1, -1, -1):
                    num[i + 1] = 0
                    if num[i] < max_index:
                        num[i] += 1
                        enough = False
                        break
            if not enough:
                res.append(pos_to_symbols(num))

    return res


if __name__ == '__main__':
    print(f'----- ListAllWords -----')

    # a_string = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    a_string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # a_string = '01'
    # a_string = 'йухи'
    alphabet = [a_string[i] for i in range(0, len(a_string))]
    min_word_len = 6
    max_word_len = 6

    # words = list_all_words(alphabet, min_word_len, max_word_len)
    words = ListAllWords(
        alphabet, min_word_len, max_word_len, reduce_to_str=True
    )
    for word_a in words:
        print(word_a)
