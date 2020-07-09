def my_histo(text_file):
    with open(f'./applications/histo/{text_file}') as f:
        words = f.read().split()

    word_tally = {}
    longest_word = 0

    # build word tally dictionary
    for word in words:
        stripped = word.strip('":;,.-+=/\|[]{}()*^&').lower()

        if not stripped:
            continue

        if len(stripped) > longest_word:
            longest_word = len(stripped)

        if stripped not in word_tally:
            word_tally[stripped] = 1

        else:
            word_tally[stripped] += 1

    # order the dictionary
    ordered = sorted(word_tally.items(), key=lambda x: (-x[1], x[0]))

    # print
    for key,value in ordered:
        # find correct spacing and hashes
        spacing = ' ' * (longest_word + 2 - len(key))
        count = '#' * value

        # print each word with tally
        print(f'{key}{spacing}{count}')


my_histo('robin.txt')