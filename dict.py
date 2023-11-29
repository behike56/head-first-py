"""_summary_
"""

import pprint


def dict_main() -> None:
    
    how_initialize()


def how_initialize() -> None:

    dict_1: dict[str, str] = {'abc': 'ppp'}

    print(dict_1['abc'])

    dict_1['abc'] = 'ooo'

    print(dict_1['abc'])

    dict_1['abc'] += 'nnn'

    print(dict_1['abc'])


def vowels_frequency(word: str) -> None:

    vowels: list[str] = ['a', 'i', 'u', 'e', 'o']

    found: dict[str, int] = {vowel: 0 for vowel in vowels}

    pprint.pprint(found)


if __name__ == "__main__":
    dict_main()
