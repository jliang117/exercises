def raindrops(number):
    ret = str(number)
    rainStr = ""
    rainStr += stringIfNumModuloBy(number,3,'Pling')
    rainStr += stringIfNumModuloBy(number,5,'Plang')
    rainStr += stringIfNumModuloBy(number,7,'Plong')

    return ret if rainStr=="" else rainStr

def stringIfNumModuloBy(num,mod,string):
	if (num % mod)==0:
		return string
	else: return ''

print(raindrops(105))
"""
assumptions
all inputs are integers
how to handle intersections?
3,5->15
5,7->35
3,7->21
does order matter?
"""