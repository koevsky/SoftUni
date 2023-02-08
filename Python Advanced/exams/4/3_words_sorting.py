def words_sorting(*args):

    words_dict = {word: sum([ord(m) for m in word]) for word in args}
    total_sum = sum([n for n in words_dict.values()])

    if total_sum % 2 == 0:
        words_dict = sorted(words_dict.items(), key=lambda x: x[0])

    else:
        words_dict = sorted(words_dict.items(), key=lambda x: -x[1])

    result = [f"{k} - {v}" for k, v in words_dict]

    return '\n'.join(result)




