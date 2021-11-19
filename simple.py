from list_all_words_generator import ListAllWords

for w in enumerate(ListAllWords(
    alphabet=range(10),
    min_word_len=3,
    max_word_len=3,
    reduce_to_str=False,
    start_from=None,
    only_unique=True
)):
    print(f'{w[0]}:  {w[1]}')