#Bifid Cipher
import fileinput
tableau = [['E','N','C','R','Y'], ['P','T','A','B','D'], ['F','G','H','I','K'], ['L','M','O','Q','S'], ['U','V','W','X','Z']]

def loc_tableau(c, tableau):
	for i in range(len(tableau)):
		if c in tableau[i]:
			loc = [i, tableau[i].index(c)]
			return loc

def search_tableau(c_list, text, tableau):
	if len(c_list) == 0:
		return text
	else:
		text += tableau[c_list[0]][c_list[1]]
		return search_tableau(c_list[2:], text, tableau)

def encrypt(m_text, tableau):
	row1, row2 = list(), list()
	for c in m_text:
		loc = loc_tableau(c, tableau)
		row1.append(loc[0])
		row2.append(loc[1])
	e_list = row1 + row2
	c_text = search_tableau(e_list, '', tableau)
	return c_text

def decrypt(c_text, tableau):
	d_list, aux = list(), list()
	for c in c_text:
		loc = loc_tableau(c, tableau)
		aux += loc
	row1 = aux[:len(aux)//2]
	row2 = aux[len(aux)//2:]
	for i in range(len(row1)):
		d_list += [row1[i], row2[i]]
	m_text = search_tableau(d_list, '', tableau)
	return m_text

def bifid(lines):
	if lines[0] == 'ENCRYPT':
		output = encrypt(lines[1], tableau)
	else:
		output = decrypt(lines[1], tableau)
	return output

lines = list()
for line in fileinput.input():
	line = line.replace('\n','')
	line = line.replace(' ','')
	lines.append(line)
print(bifid(lines))
