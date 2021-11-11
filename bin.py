from list_all_words_generator import ListAllWords

if __name__ == '__main__':
    print(f'----- ListAllBinaries -----')

    alphabet = ['0', '1']
    min_word_len = 1
    max_word_len = 32
    start_from_str = '11111100110000000110110'
    start_from = [x for x in start_from_str]

    with open('f.txt','w') as f:
        words = ListAllWords(
            alphabet, min_word_len, max_word_len, reduce_to_str=True
            , start_from=start_from
        )
        for word_a in words:
            print(word_a)
            # f.write(word_a+"\n")
