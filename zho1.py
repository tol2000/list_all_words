from list_all_words_generator import ListAllWords
from itertools import combinations, combinations_with_replacement

if __name__ == '__main__':
    print(f'----- ListAllBinaries -----')

    alphabet = ['глав', 'внеш', 'прод', 'сов', 'мор', 'транс', 'авто']
    a = "каждый охотник желает знать где сидит фазан сегодня не он лишь может смотреть в завтрашний день карл у клара украл кораллы а кларнет нужно вернуть"
    alphabet = [f'{x}' for x in a.split(' ')]
    print(alphabet)
    min_word_len = 5
    max_word_len = 5
    start_from_str = None
    start_from = None
    # start_from = [x for x in start_from_str]

    words = ListAllWords(
        alphabet, min_word_len, max_word_len
        , reduce_to_str=False
        , start_from=start_from
        , only_unique=True
    )

    words1 = combinations_with_replacement(alphabet, 20)

    with open('out.txt', 'w') as f:
        for word_a in words:
            word_a = 3 * (' '.join(word_a) + '    ')
            print(word_a)
            #f.write(word_a+'\n')
