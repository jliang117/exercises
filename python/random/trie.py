
END_CHAR = '*'


def makeTrie(words):
  root = dict()
  for word in words:
    temp = root
    for letter in word:
      temp = temp.setdefault(letter,{})
    temp[END_CHAR] = END_CHAR
  return root

def findKey(trie, key):
  subTrie = trie
  for letter in key:
    if letter in subTrie:
      # we found a match, keep going down
      subTrie = subTrie[letter]
    else:
      # no perfect match, string isn't there, can we still keep going based on other indicators? 
      return False
  else:
    if END_CHAR in subTrie:
      return True
    return False
    

def insertKey(trie,key):
  if findKey(trie,key):
    return trie
  subTrie = trie
  for letter in key:
    if letter in subTrie:
      subTrie = subTrie[letter]
    else:
      subTrie = subTrie.setdefault(letter,{})
  subTrie[END_CHAR] = END_CHAR
  return trie

def getLongestPath(trie):
  retVal = ""
  subTrie = trie
  while len(subTrie.keys()) == 1:
    retVal = retVal + subTrie.keys()[0]
    subTrie = subTrie.get(subTrie.keys()[0])
  return retVal