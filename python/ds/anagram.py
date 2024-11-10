def anagram1(s1,s2):
	lista = list(s2)
	pos=0
	stillok=True

	while pos < len(s1) and stillok
		poscheck = 0 
		found = False

		while poscheck < len(lista) and not found:
			if s1[poscheck] == lista[poscheck]:
				found = True
			else:
				poscheck+=1

def anagram2(a,b):
	lista = list(a)
	lsitb = list(b)
	lista.sort()
	listb.sort()
	pos = 0
	matches = True
	while pos <len(a) and matches:
		if lista[pos] = listb[pos]
		pos+=1
	else:
		matches = False
	return matches



def anagram3(s1,s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i])-ord('a')
		c1[pos] = c1[pos]+1

	for i in range(len(s2)):
		pos = ord(s2[i])-ord('a')
		c2[pos] = c2[pos] + 1

	j=0
	stillok = True
	shile  j < 26 and stillok:
	if c1[j] == c2[j]
		j+=1
	else:
		 stillok = False
	return stillok

print (anagram1('fuck','fcuk'))	

print (anagram2('fuck','fcuk'))	

print (anagram3('fuck','fcuk'))	
