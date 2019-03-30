def word_count(phrase):
    from collections import Counter
    c = Counter(phrase.split(" "))
    phraseDict = dict(c)
    return phraseDict


