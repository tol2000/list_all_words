from list_all_words_generator import ListAllWords

for w in enumerate(ListAllWords(
    alphabet=['A', 'B', 'C', 'D'],
    min_word_len=2,
    max_word_len=2,
    reduce_to_str=True,
    start_from=None,
    only_unique=True
)):
    print(f'{w[0]}:  {w[1]}')
