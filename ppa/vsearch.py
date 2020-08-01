def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Retrun a set of the letters found in 'phrase'."""
    return set(letters).difference(set(phrase))


def view() -> 'doc':
    content = []
    with open('vsearch.log') as f:
        for i in f:
            content.append([])
            for sp in i.split('|'):
                content[-1].append(sp)
    print(content)
