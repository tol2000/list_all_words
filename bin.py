from list_all_words_generator import ListAllWords

if __name__ == '__main__':
    print(f'----- ListAllBinaries -----')

    alphabet = ['0', '1']
    min_word_len = 1
    max_word_len = 32
    start_from_str = '10101110100101110000001'
    start_from = [x for x in start_from_str]

    words = ListAllWords(
        alphabet, min_word_len, max_word_len, reduce_to_str=True
        , start_from=start_from
    )
    for word_a in words:
        print(word_a)
