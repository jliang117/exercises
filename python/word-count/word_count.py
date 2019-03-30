from collections import Counter
def word_count(phrase):
	phrase = normalize(phrase)
	pList = phrase.split()
	pList = removeQuotes(pList)
	c = Counter(pList)
	phraseDict = dict(c)
	return phraseDict

def removeQuotes(phraseList):
	return [word.strip('\'') for word in phraseList]

def normalize(phrase):
	phrase = normalizeDelim(phrase)
	phrase = normalizeCase(phrase)
	phrase = removePunc(phrase)
	return phrase

def normalizeDelim(phrase):
	delimSet = {'\n',' ',':',',','_'}
	for ele in delimSet:
		phrase = phrase.replace(ele," ")
	return phrase



def removePunc(phrase):
	puncSet = {'.','!','&','@','$','%','^','&'}
	for ele in puncSet:
		phrase = phrase.replace(ele,"")
	return phrase

def normalizeCase(phrase):
	return phrase.lower()


phrase = "Joe can't tell between 'large' and large."
# print(normalize(phrase))

print(word_count(phrase))
