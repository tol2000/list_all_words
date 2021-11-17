from list_all_words_generator import ListAllWords

if __name__ == '__main__':
    print(f'----- ListAllBinaries -----')

    alphabet = ['глав', 'внеш', 'прод', 'сов', 'мор', 'транс', 'авто']
    min_word_len = 2
    max_word_len = 10
    start_from_str = None
    start_from = None
    # start_from = [x for x in start_from_str]

    words = ListAllWords(
        alphabet, min_word_len, max_word_len, reduce_to_str=True
        , start_from=start_from
        , only_unique=True
    )
    
    with open('out.txt', 'w') as f:
        for word_a in words:
            print(word_a)
            f.write(word_a+'\n')
