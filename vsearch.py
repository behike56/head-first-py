def search4vowels(phrase: str) -> set:
    vowels = set('aiueo')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) -> set:
    return set(letters).intersection(set(phrase))
