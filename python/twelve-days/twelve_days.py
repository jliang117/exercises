def recite(start_verse, end_verse):
    phraseDict = buildPhraseDict()
    dayDict = buildDayDict()
    verse = "On the %s day of Christmas my true love gave to me: " % dayDict.get(start_verse)

    output = ""
    output += verse
    if start_verse == 1:
    	output += phraseDict.get(0)
    	outarr = [output]
    	return outarr
    while start_verse != 0:
    	output += phraseDict.get(start_verse)
    	start_verse = start_verse-1
    outArr = [output]
    return outArr



def buildPhraseDict():
	phraseDict = {12:"twelve Drummers Drumming, ",
	11: "eleven Pipers Piping, ",
	10: "ten Lords-a-Leaping, ",
	9: "nine Ladies Dancing, ",
	8: "eight Maids-a-Milking, ",
	7: "seven Swans-a-Swimming, ",
	6: "six Geese-a-Laying, ",
	5: "five Gold Rings, ",
	4: "four Calling Birds, ",
	3: "three French Hens, ",
	2: "two Turtle Doves, ",
	1:  "and a Partridge in a Pear Tree.",
	0:  "a Partridge in a Pear Tree."}
	return phraseDict

def buildDayDict():
	phraseDict = {12:"twelfth",
	11: "eleventh",
	10: "tenth",
	9: "ninth",
	8: "eighth",
	7: "seventh",
	6: "sixth",
	5: "fifth",
	4: "fourth",
	3: "third",
	2: "second",
	1:  "first"}
	return phraseDict
print(recite(1,4))